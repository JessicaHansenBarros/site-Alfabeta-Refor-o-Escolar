import os
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

CAMINHO_DB =  os.path.join(os.path.dirname(__file__), "alfabeta.db")

DATABASE_URL = f"sqlite:///{CAMINHO_DB}"

engine = create_engine(DATABASE_URL, echo=False)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass

def criar_tabelas():
    import db.models
    Base.metadata.create_all(bind=engine)
