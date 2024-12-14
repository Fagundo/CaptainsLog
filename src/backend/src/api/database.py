import os
from sqlmodel import Session, create_engine
from contextlib import contextmanager
from src.backend.models import SQLModel

# Replace with actual database URL
DATABASE_URL = os.getenv(
    'DATABASE_URL',
    "postgresql://username:password@localhost/dbname"
) 

engine = create_engine(DATABASE_URL)

# Context manager to manage DB sessions
@contextmanager
def get_db():
    with Session(engine) as session:
        yield session

# Function to create tables
def create_db():
    SQLModel.metadata.create_all(engine)
