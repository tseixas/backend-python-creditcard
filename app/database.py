from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from app.config import settings

USER = settings.db_user
PASSWORD = settings.db_password
HOST = settings.db_host
NAME = settings.db_name

DATABASE_URL = f"postgresql://{USER}:{PASSWORD}@{HOST}/{NAME}"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

Base = declarative_base()
