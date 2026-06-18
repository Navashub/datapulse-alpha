"""
Application configuration.

All settings are loaded from environment variables.
Never hardcode secrets — always use the .env file locally
and environment variables in production.
"""

from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Central configuration for DataPulse AI.

    Pydantic-settings automatically reads values from
    environment variables or a .env file.
    """

    # Application
    app_name: str = "DataPulse AI"
    app_version: str = "0.1.0"
    debug: bool = False

    # Database
    database_url: str

    # OpenAI
    openai_api_key: str

    # LanceDB
    lancedb_uri: str = "./lancedb_data"

    # Documents
    documents_dir: str = "./documents"

    class Config:
        env_file = ".env"
        case_sensitive = False


# Single instance used across the entire app
# Import this wherever you need settings:
# from app.config import settings
settings = Settings()