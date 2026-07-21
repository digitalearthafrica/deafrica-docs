"""Download a POEditor translation file."""

from __future__ import annotations

import argparse
import logging
import os
from pathlib import Path

from poeditor import POEditorAPI


LOGGER = logging.getLogger(__name__)

DEFAULT_LANGUAGE = "fr"
DEFAULT_FILE_TYPE = "po"
DEFAULT_OUTPUT = Path("locales/fr/LC_MESSAGES/docs.po")


def download_translation(
    output_path: Path,
    project_id: int,
    api_token: str,
    language_code: str = DEFAULT_LANGUAGE,
    file_type: str = DEFAULT_FILE_TYPE,
) -> Path:
    """Download a translation file from POEditor.

    Parameters
    ----------
    output_path:
        Local destination for the downloaded translation.
    project_id:
        POEditor project identifier.
    api_token:
        POEditor API token.
    language_code:
        Translation language code, such as ``fr``.
    file_type:
        POEditor export format, such as ``po``.

    Returns
    -------
    pathlib.Path
        The absolute path of the downloaded file.
    """
    output_path = output_path.expanduser().resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    client = POEditorAPI(api_token=api_token)

    LOGGER.info(
        "Downloading %s translation for language %s to %s",
        file_type,
        language_code,
        output_path,
    )

    client.export(
        project_id=project_id,
        language_code=language_code,
        file_type=file_type,
        local_file=str(output_path),
    )

    if not output_path.exists():
        raise RuntimeError(
            f"POEditor export completed, but the file was not created: "
            f"{output_path}"
        )

    LOGGER.info("Translation downloaded successfully.")
    return output_path


def get_required_environment_variable(name: str) -> str:
    """Return a required environment variable or raise a clear error."""
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Required environment variable {name!r} is not set."
        )

    return value


def parse_arguments() -> argparse.Namespace:
    """Parse command-line arguments."""
    parser = argparse.ArgumentParser(
        description="Download a translation file from POEditor."
    )

    parser.add_argument(
        "--project-id",
        type=int,
        default=None,
        help=(
            "POEditor project ID. Defaults to the "
            "POEDITOR_PROJECT_ID environment variable."
        ),
    )

    parser.add_argument(
        "--language",
        default=DEFAULT_LANGUAGE,
        help=f"Language code. Default: {DEFAULT_LANGUAGE}",
    )

    parser.add_argument(
        "--file-type",
        default=DEFAULT_FILE_TYPE,
        help=f"Export file type. Default: {DEFAULT_FILE_TYPE}",
    )

    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"Output path. Default: {DEFAULT_OUTPUT}",
    )

    return parser.parse_args()


def main() -> None:
    """Run the POEditor translation download."""
    args = parse_arguments()

    api_token = get_required_environment_variable("POEDITOR_API_TOKEN")

    project_id = args.project_id
    if project_id is None:
        project_id_text = get_required_environment_variable(
            "POEDITOR_PROJECT_ID"
        )

        try:
            project_id = int(project_id_text)
        except ValueError as exc:
            raise RuntimeError(
                "POEDITOR_PROJECT_ID must be a valid integer."
            ) from exc

    try:
        downloaded_file = download_translation(
            output_path=args.output,
            project_id=project_id,
            api_token=api_token,
            language_code=args.language,
            file_type=args.file_type,
        )
    except Exception:
        LOGGER.exception("Failed to download the translation.")
        raise

    print(f"Translation downloaded to: {downloaded_file}")


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(levelname)s: %(message)s",
    )

    main()