from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from ..core.config import settings
from app.models.base import Base

engine = create_engine(settings.DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Bind the engine to the Base metadata
Base.metadata.bind = engine

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()