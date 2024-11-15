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
if __name__ == '__main__':
    project_id = '715168' #os.environ['POEDITOR_PROJECT_ID']
    api_token = '17a7337c0def1d5df25624819906e85c' #os.environ['POEDITOR_API_TOKEN']
    
    file_path = 'locales/fr/LC_MESSAGES/docs.po'
    print(f"Downloading translation to {file_path}")
    
    download_translation(file_path, project_id, api_token)
