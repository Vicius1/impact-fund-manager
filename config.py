from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8"
    )

    DATABASE_URL: str
    GOOGLE_CREDENTIALS_FILE: str
    GOOGLE_DRIVE_PARENT_FOLDER_ID: str

settings = Settings()