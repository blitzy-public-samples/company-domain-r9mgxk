from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    PROJECT_NAME: str = "AI-Powered Job Application Assistant"
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = "your-secret-key-here"  # Change this in production
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    DATABASE_URL: str = "sqlite:///./test.db"  # Change this in production
    GOOGLE_APPLICATION_CREDENTIALS: Optional[str] = None
    GOOGLE_CLOUD_PROJECT: str = "your-google-cloud-project-id"
    GOOGLE_CLOUD_STORAGE_BUCKET: str = "your-google-cloud-storage-bucket-name"
    SENDGRID_API_KEY: str = "your-sendgrid-api-key"
    EMAIL_FROM_ADDRESS: str = "noreply@example.com"
    LINKEDIN_API_KEY: str = "your-linkedin-api-key"
    HUNTER_API_KEY: str = "your-hunter-api-key"
    CLEARBIT_API_KEY: str = "your-clearbit-api-key"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"

settings = Settings()