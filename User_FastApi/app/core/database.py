from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker , declarative_base
from app.core.config import Database_URL

engine=create_engine(Database_URL)
SessionLocal=sessionmaker(autoflush=False,autocommit=False, bind=engine)

Base=declarative_base()