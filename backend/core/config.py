import os

class Settings:
    DATABASE_URL: str = os.getenv("DATABASE_URL")
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")
    ACCESS_EXPIRE_MIN: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", 15))
    REFRESH_EXPIRE_DAYS: int(os.getenv("REFRESH_TOKEN_EXPIRE_DAYS", 15))

settings = Settings()