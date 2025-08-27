import asyncio
from google.oauth2 import service_account
from googleapiclient.discovery import build, Resource

from config import settings

SCOPES = ["https://www.googleapis.com/auth/drive"]

def _get_drive_service() -> Resource:
    """
    Função auxiliar síncrona para autenticar e construir o objeto de serviço do Drive.
    """
    creds = service_account.Credentials.from_service_account_file(
        settings.GOOGLE_CREDENTIALS_FILE, scopes=SCOPES
    )
    service = build("drive", "v3", credentials=creds)
    return service


async def create_folder(folder_name: str) -> str | None:
    """
    Cria uma nova pasta no Google Drive dentro da pasta pai definida na configuração.

    Args:
        folder_name: O nome da nova pasta a ser criada.

    Returns:
        O ID da pasta recém-criada, ou None em caso de erro.
    """
    try:
        service = _get_drive_service()

        file_metadata = {
            "name": folder_name,
            "mimeType": "application/vnd.google-apps.folder",
            "parents": [settings.GOOGLE_DRIVE_PARENT_FOLDER_ID],
        }

        created_file = await asyncio.to_thread(
            service.files()
            .create(body=file_metadata, fields="id")
            .execute
        )

        folder_id = created_file.get("id")
        print(f"Pasta '{folder_name}' criada com sucesso. ID: {folder_id}")
        return folder_id

    except Exception as e:
        print(f"Ocorreu um erro ao criar a pasta no Google Drive: {e}")
        return None