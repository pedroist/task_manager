"""
Import all models here to ensure they are registered with SQLAlchemy
before creating the tables.
"""
from app.db.base import Base

# Import all models here
# Example:
# from .user import User
# from .task import Task

# This allows us to import all models from app.models.base
__all__ = [
    "Base",
    # Add model names here as we create them
    # "User",
    # "Task",
]
