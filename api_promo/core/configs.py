from typing import List
import os
from starlette.config import Config
from starlette.datastructures import Secret

from pydantic import BaseSettings
from sqlalchemy.ext.declarative import declarative_base

class Settings(BaseSettings):

    API_V1_STR: str = '/api/v1'

    DB_URL: str = 'postgresql+asyncpg://'
    #DB_URL: str = 'postgresql+asyncpg://postgres:1702@localhost:5432/promocao'
    DBBaseModel = declarative_base()

    JWT_SECRET: str = ''

    """
    import secrets

    token: str = secrets.token_urlsafe(32)
    """
    ALGORITHM: str = 'HS256'
    # 60 minutos * 24 horas * 7 dias => 1 semana
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 7

    class Config:
        case_sensitive = True


settings: Settings = Settings()
