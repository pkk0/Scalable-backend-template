from pydantic import BaseSettings, AnyHttpUrl

class Settings(BaseSettings):
    TITLE: str = 'Scalable API Template'
    VERSION: str = 'v0.1'
    API_DOCS_ENABLED: bool = False
    BACKEND_CORS_ORIGINS: list[AnyHttpUrl] = []

settings = Settings()