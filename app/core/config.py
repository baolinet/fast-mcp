from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_ENV: str
    SECRET_KEY: str
    OPENAI_API_KEY: str
    OPENAI_BASE_URL: str
    OPENAI_MODEL: str
    PORT: int

    class Config:
        env_file = ".env"

settings = Settings()
