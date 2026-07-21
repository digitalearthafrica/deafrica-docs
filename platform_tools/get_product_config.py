"""Build ``odc.stac.load`` configuration from ODC product definitions.

This module downloads an Open Data Cube product-definition YAML document from
the Digital Earth Africa or Digital Earth Australia Metadata Explorer and
converts its measurement metadata into an ``odc.stac.load(..., stac_cfg=...)``
configuration dictionary.

Example
-------
>>> config = get_product_config("s2_l2a", profile="deafrica")
>>> # data = odc.stac.load(items, stac_cfg=config, ...)
"""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any, Final, Literal
import re

import requests
import yaml


Profile = Literal["deafrica", "deaustralia"]

DEFAULT_TIMEOUT: Final[tuple[float, float]] = (5.0, 30.0)
_PRODUCT_NAME_PATTERN: Final[re.Pattern[str]] = re.compile(r"^[A-Za-z0-9_.-]+$")

_PROFILE_SETTINGS: Final[dict[Profile, dict[str, str]]] = {
    "deafrica": {
        "name": "Digital Earth Africa",
        "products_url": "https://explorer.digitalearth.africa/products",
    },
    "deaustralia": {
        "name": "Digital Earth Australia",
        "products_url": "https://explorer.sandbox.dea.ga.gov.au/products",
    },
}


class ProductConfigError(RuntimeError):
    """Base exception raised when a product configuration cannot be created."""


class ProductNotFoundError(ProductConfigError):
    """Raised when a product is not available in the selected explorer."""


class InvalidProductDefinitionError(ProductConfigError):
    """Raised when a downloaded product definition is malformed or incomplete."""


def _validate_product_name(product_name: str) -> str:
    """Validate and normalise a product name."""
    if not isinstance(product_name, str):
        raise TypeError("product_name must be a string.")

    product_name = product_name.strip()

    if not product_name:
        raise ValueError("product_name cannot be empty.")

    if not _PRODUCT_NAME_PATTERN.fullmatch(product_name):
        raise ValueError(
            "product_name may contain only letters, numbers, underscores, "
            "hyphens, and full stops."
        )

    return product_name


def _get_profile_settings(profile: str) -> dict[str, str]:
    """Return explorer settings for a supported profile."""
    try:
        return _PROFILE_SETTINGS[profile]  # type: ignore[index]
    except KeyError as exc:
        supported = ", ".join(repr(name) for name in _PROFILE_SETTINGS)
        raise ValueError(
            f"Invalid profile {profile!r}. Supported profiles are: {supported}."
        ) from exc


def _download_product_definition(
    product_name: str,
    *,
    profile: Profile,
    session: requests.Session,
    timeout: tuple[float, float],
) -> Mapping[str, Any]:
    """Download and safely parse one product-definition YAML document."""
    settings = _get_profile_settings(profile)
    products_url = settings["products_url"]
    definition_url = f"{products_url}/{product_name}.odc-product.yaml"

    try:
        response = session.get(definition_url, timeout=timeout)
    except requests.Timeout as exc:
        raise ProductConfigError(
            f"Timed out while downloading product definition for "
            f"{product_name!r} from {settings['name']}."
        ) from exc
    except requests.RequestException as exc:
        raise ProductConfigError(
            f"Could not download product definition for {product_name!r} "
            f"from {settings['name']}: {exc}"
        ) from exc

    if response.status_code == 404:
        raise ProductNotFoundError(
            f"Product {product_name!r} was not found in the "
            f"{settings['name']} Metadata Explorer. See {products_url}."
        )

    try:
        response.raise_for_status()
    except requests.HTTPError as exc:
        raise ProductConfigError(
            f"The Metadata Explorer returned HTTP {response.status_code} "
            f"for {definition_url}."
        ) from exc

    try:
        product_definition = yaml.safe_load(response.text)
    except yaml.YAMLError as exc:
        raise InvalidProductDefinitionError(
            f"The YAML definition for {product_name!r} could not be parsed."
        ) from exc

    if not isinstance(product_definition, Mapping):
        raise InvalidProductDefinitionError(
            f"The definition for {product_name!r} is not a YAML mapping."
        )

    return product_definition


def _build_stac_config(
    product_name: str,
    product_definition: Mapping[str, Any],
) -> dict[str, dict[str, Any]]:
    """Convert ODC measurement metadata into an odc-stac configuration."""
    measurements = product_definition.get("measurements")

    if not isinstance(measurements, list) or not measurements:
        raise InvalidProductDefinitionError(
            f"The definition for {product_name!r} has no valid "
            "'measurements' list."
        )

    assets: dict[str, dict[str, Any]] = {}
    aliases: dict[str, str] = {}

    for index, measurement in enumerate(measurements):
        if not isinstance(measurement, Mapping):
            raise InvalidProductDefinitionError(
                f"Measurement {index} for {product_name!r} is not a mapping."
            )

        name = measurement.get("name")
        data_type = measurement.get("dtype")

        if not isinstance(name, str) or not name:
            raise InvalidProductDefinitionError(
                f"Measurement {index} for {product_name!r} has no valid name."
            )

        if not isinstance(data_type, str) or not data_type:
            raise InvalidProductDefinitionError(
                f"Measurement {name!r} for {product_name!r} has no valid dtype."
            )

        asset: dict[str, Any] = {"data_type": data_type}

        # Preserve optional values only when they are present in the definition.
        if "nodata" in measurement:
            asset["nodata"] = measurement["nodata"]

        units = measurement.get("units")
        if units is not None:
            asset["unit"] = units

        assets[name] = asset

        measurement_aliases = measurement.get("aliases", [])
        if measurement_aliases is None:
            measurement_aliases = []

        if not isinstance(measurement_aliases, list):
            raise InvalidProductDefinitionError(
                f"Aliases for measurement {name!r} must be a list."
            )

        for alias in measurement_aliases:
            if not isinstance(alias, str) or not alias:
                raise InvalidProductDefinitionError(
                    f"Measurement {name!r} contains an invalid alias."
                )

            existing_target = aliases.get(alias)
            if existing_target is not None and existing_target != name:
                raise InvalidProductDefinitionError(
                    f"Alias {alias!r} is assigned to both "
                    f"{existing_target!r} and {name!r}."
                )

            aliases[alias] = name

    collection_config: dict[str, Any] = {"assets": assets}
    if aliases:
        collection_config["aliases"] = aliases

    return {product_name: collection_config}


def get_product_config(
    product_name: str,
    profile: Profile = "deafrica",
    *,
    timeout: tuple[float, float] = DEFAULT_TIMEOUT,
    session: requests.Session | None = None,
) -> dict[str, dict[str, Any]]:
    """Return an ``odc.stac.load`` configuration for an ODC product.

    Parameters
    ----------
    product_name:
        Product name used by the selected Metadata Explorer, for example
        ``"s2_l2a"``.
    profile:
        Metadata Explorer profile. Use ``"deafrica"`` for Digital Earth Africa
        or ``"deaustralia"`` for Digital Earth Australia.
    timeout:
        Requests connect and read timeouts, in seconds.
    session:
        Optional reusable :class:`requests.Session`. A temporary session is
        created and closed when this argument is omitted.

    Returns
    -------
    dict
        A dictionary suitable for ``odc.stac.load(..., stac_cfg=config)``.

    Raises
    ------
    ValueError
        If the product name or profile is invalid.
    ProductNotFoundError
        If the product does not exist in the selected explorer.
    ProductConfigError
        If downloading or processing the definition fails.
    """
    validated_name = _validate_product_name(product_name)
    _get_profile_settings(profile)

    owns_session = session is None
    active_session = session or requests.Session()

    try:
        product_definition = _download_product_definition(
            validated_name,
            profile=profile,
            session=active_session,
            timeout=timeout,
        )
        return _build_stac_config(validated_name, product_definition)
    finally:
        if owns_session:
            active_session.close()


if __name__ == "__main__":
    # Small manual example. Network access is required.
    from pprint import pprint

    pprint(get_product_config("s2_l2a"))
