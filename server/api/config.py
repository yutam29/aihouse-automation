from functools import lru_cache

from pydantic import validator
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """
    Settings for the FastAPI server.
    """

    # AUTH0 configuration
    AUTH0_DOMAIN: str
    AUTH0_AUDIENCE: str

    # CORS
    CLIENT_ORIGIN_URL: str

    # FastAPI configuration
    PORT: int
    RELOAD: bool

    @classmethod
    @validator("CLIENT_ORIGIN_URL", "AUTH0_AUDIENCE", "AUTH0_DOMAIN")
    def check_not_empty(cls, v):
        assert v != "", f"{v} is not defined"
        return v

    class Config:
        """
        Tell BaseSettings the env file path
        """

        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache()
def get_settings(**kwargs) -> Settings:
    """
    Get settings. ready for FastAPI's Depends.

    lru_cache - cache the Settings object per arguments given.
    """
    settings = Settings(**kwargs)
    return settings
