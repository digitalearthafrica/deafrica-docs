import os
from pathlib import Path
from poeditor import POEditorAPI


def download_translation(file_path, project_id, api_token):
    client = POEditorAPI(api_token=api_token)

    os.makedirs(Path(file_path).absolute().parent, exist_ok=True)

    client.export(
        project_id=project_id,
        language_code='fr',
        file_type='po',
        local_file=file_path,
    )


project_id = os.environ['POEDITOR_PROJECT_ID']
api_token = os.environ['POEDITOR_API_TOKEN']

file_path = 'locales/fr/LC_MESSAGES/docs.po'
print(f"Downloading translation to {file_path}")

download_translation(file_path, project_id, api_token)
