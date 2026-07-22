import json
import os
import sys

import requests


API_URL = "https://api.poeditor.com/v2/translations/automatic"


def required_environment_variable(name: str) -> str:
    value = os.environ.get(name)

    if not value:
        raise RuntimeError(f"{name} is not configured.")

    return value


def main() -> None:
    api_token = required_environment_variable(
        "POEDITOR_API_TOKEN"
    )
    project_id = required_environment_variable(
        "POEDITOR_PROJECT_ID"
    )

    source_language = os.environ.get(
        "POEDITOR_SOURCE_LANGUAGE",
        "en",
    )
    target_language = os.environ.get(
        "POEDITOR_TARGET_LANGUAGE",
        "fr",
    )
    provider = os.environ.get(
        "POEDITOR_TRANSLATION_PROVIDER",
        "deepl",
    )

    payload = {
        "api_token": api_token,
        "id": project_id,
        "source_language": source_language,
        "provider_source_language": source_language,
        "provider": provider,
        "target_languages": json.dumps(
            {
                target_language: target_language,
            }
        ),
    }

    response = requests.post(
        API_URL,
        data=payload,
        timeout=120,
    )
    response.raise_for_status()

    result = response.json()

    status = (
        result.get("response", {})
        .get("status")
    )

    if status != "success":
        print(result)
        raise RuntimeError(
            "POEditor automatic translation failed."
        )

    print(
        f"Automatic translation completed for "
        f"{target_language} using {provider}."
    )


if __name__ == "__main__":
    try:
        main()
    except Exception as error:
        print(
            f"Automatic translation error: {error}",
            file=sys.stderr,
        )
        raise