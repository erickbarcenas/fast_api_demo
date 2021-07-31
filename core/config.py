import os
from pathlib import Path
from dotenv import load_dotenv
from py2neo import Graph

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)


class Settings:
    PROJECT_TITLE: str = "Shugar App"
    PROJECT_DESCRIPTION = "RestFul Shugar App API"
    PROJECT_VERSION: str = "1.0.0"

    NEO4J_USER: str = os.getenv("NEO4J_USER")
    NEO4J_PASSWORD = os.getenv("NEO4J_PASSWORD")
    NEO4J_SERVER: str = os.getenv("NEO4J_SERVER")
    NEO4J_PORT: str = os.getenv("NEO4J_PORT")
    NEO4J_DB: str = os.getenv("NEO4J_DB")


    # SECRET_KEY : str = os.getenv("SECRET_KEY")
    # ALGORITHM = "HS256"
    # ACCESS_TOKEN_EXPIRE_MINUTES = 30
    # TEST_USER_EMAIL = "test@example.com"


settings = Settings()
