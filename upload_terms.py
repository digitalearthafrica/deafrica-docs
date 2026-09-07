import os
import sys
from pathlib import Path
from typing import Any

import requests


POEDITOR_UPLOAD_URL = (
    "https://api.poeditor.com/v2/projects/upload"
)

POT_FILE = Path("_build/docs.pot")


def require_environment_variable(name: str) -> str:
    """Return a required environment variable."""
    value = os.environ.get(name)

    if not value:
        raise RuntimeError(
            f"{name} is not configured."
        )

    return value


def upload_terms(
    api_token: str,
    project_id: str,
    pot_file: Path,
) -> dict[str, Any]:
    """Upload a POT file to POEditor."""

    if not pot_file.is_file():
        raise FileNotFoundError(
            f"POT file not found: {pot_file}"
        )

    if pot_file.stat().st_size == 0:
        raise RuntimeError(
            f"POT file is empty: {pot_file}"
        )

    data = {
        "api_token": api_token,
        "id": project_id,
        "updating": "terms",

        # Delete POEditor terms that no longer exist in the POT file.
        "sync_terms": "1",

        # Explicitly identify the file as a Gettext POT catalogue.
        "type": "pot",
    }

    with pot_file.open("rb") as file_handle:
        files = {
            "file": (
                pot_file.name,
                file_handle,
                "text/x-gettext-translation-template",
            ),
        }

        response = requests.post(
            POEDITOR_UPLOAD_URL,
            data=data,
            files=files,
            timeout=180,
        )

    response.raise_for_status()

    result = response.json()
    api_response = result.get("response", {})

    if api_response.get("status") != "success":
        message = api_response.get(
            "message",
            "Unknown POEditor API error.",
        )

        raise RuntimeError(
            f"POEditor upload failed: {message}"
        )

    return result


def main() -> None:
    """Upload the generated documentation terms."""

    api_token = require_environment_variable(
        "POEDITOR_API_TOKEN"
    )
    project_id = require_environment_variable(
        "POEDITOR_PROJECT_ID"
    )

    print(
        f"Uploading translation terms from {POT_FILE}..."
    )

    result = upload_terms(
        api_token=api_token,
        project_id=project_id,
        pot_file=POT_FILE,
    )

    terms = (
        result.get("result", {})
        .get("terms", {})
    )

    print("POEditor terms uploaded successfully.")
    print(
        "Parsed: "
        f"{terms.get('parsed', 0)}, "
        "Added: "
        f"{terms.get('added', 0)}, "
        "Updated: "
        f"{terms.get('updated', 0)}, "
        "Deleted: "
        f"{terms.get('deleted', 0)}"
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(
            f"ERROR: Failed to update POEditor terms: "
            f"{error}",
            file=sys.stderr,
        )
        raise