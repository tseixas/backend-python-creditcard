from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:postgres@127.0.0.1/creditcard"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

Base = declarative_base()
