from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict

APP_VERSION = "0.1.0"


class Settings(BaseSettings):
    """Configuración de entorno para StudyTracker."""

    database_url: str = "postgresql+psycopg://studytracker:cambia_esta_clave_local@db:5432/studytracker_db"
    auto_seed: bool = True

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


@lru_cache
def get_settings() -> Settings:
    """Devuelve la instancia cacheada de configuración."""
    return Settings()
