"""
Import all models here to ensure they are registered with SQLAlchemy
before creating the tables.
"""
from app.db.base import Base
from .user import User
from .task import Task

# This allows us to import all models from app.models.base
__all__ = [
    # Add model names here as we create them
    "Base",
    "User",
    "Task"
]
