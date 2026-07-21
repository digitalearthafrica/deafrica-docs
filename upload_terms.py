"""Upload a Sphinx POT file to POEditor and synchronise project terms."""

from __future__ import annotations

import logging
import os
from pathlib import Path
from typing import Any

from poeditor import POEditorAPI


LOGGER = logging.getLogger(__name__)

DEFAULT_POT_FILE = Path("_build/docs.pot")


def get_required_env(name: str) -> str:
    """Return a required environment variable."""
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Required environment variable {name!r} is not set."
        )

    return value


def get_project_details(
    client: POEditorAPI,
    project_id: int,
) -> dict[str, Any]:
    """Retrieve and validate POEditor project details."""
    project = client.view_project_details(project_id)

    if not isinstance(project, dict):
        raise RuntimeError(
            "POEditor returned an unexpected project-details response."
        )

    return project


def print_project_summary(
    project: dict[str, Any],
    label: str,
) -> None:
    """Print a concise project summary."""
    name = project.get("name", "Unknown project")
    project_id = project.get("id", "unknown")
    terms = project.get("terms", "unknown")

    print(
        f"{label}: {name} "
        f"(ID: {project_id}) has {terms} terms."
    )


def update_project_terms(
    client: POEditorAPI,
    project_id: int,
    pot_file: Path,
    *,
    sync_terms: bool = True,
) -> dict[str, Any]:
    """Upload a POT file and update POEditor terms."""
    pot_file = pot_file.expanduser().resolve()

    if not pot_file.is_file():
        raise FileNotFoundError(
            f"POT file was not found: {pot_file}"
        )

    LOGGER.info("Uploading translation terms from %s", pot_file)

    result = client.update_terms(
        project_id=project_id,
        file_path=str(pot_file),
        sync_terms=sync_terms,
    )

    if not isinstance(result, dict):
        raise RuntimeError(
            "POEditor returned an unexpected update response."
        )

    return result


def print_update_results(result: dict[str, Any]) -> None:
    """Display the term-update statistics."""
    terms = result.get("terms")

    if not isinstance(terms, dict):
        LOGGER.warning(
            "No term statistics were returned by POEditor."
        )
        return

    print("Terms updated:")

    for key, value in terms.items():
        print(f"  {key}: {value}")


def main() -> None:
    """Synchronise Sphinx translation terms with POEditor."""
    project_id_text = get_required_env("POEDITOR_PROJECT_ID")
    api_token = get_required_env("POEDITOR_API_TOKEN")

    try:
        project_id = int(project_id_text)
    except ValueError as exc:
        raise RuntimeError(
            "POEDITOR_PROJECT_ID must be a valid integer."
        ) from exc

    client = POEditorAPI(api_token=api_token)

    project_before = get_project_details(
        client,
        project_id,
    )
    print_project_summary(
        project_before,
        "Before update",
    )

    update_result = update_project_terms(
        client=client,
        project_id=project_id,
        pot_file=DEFAULT_POT_FILE,
        sync_terms=True,
    )
    print_update_results(update_result)

    project_after = get_project_details(
        client,
        project_id,
    )
    print_project_summary(
        project_after,
        "After update",
    )


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    try:
        main()
    except Exception:
        LOGGER.exception(
            "Failed to update POEditor terms."
        )
        raise