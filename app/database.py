import os
from sqlmodel import create_engine, SQLModel, Session
from dotenv import load_dotenv

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

connect_args = {"check_same_thread": False} if "sqlite" in DATABASE_URL else {}

engine = create_engine(DATABASE_URL, connect_args=connect_args)

def lifespan(app):
    SQLModel.metadata.create_all(engine)  
    yield

def get_session():
    session = Session(engine)
    try:
        yield session  
    finally:
        session.close()  

