from sqlalchemy import Boolean, Column, Integer, String, Enum
import enum
from app.db.base import Base


class UserRole(str, enum.Enum):
    MANAGER = "manager"
    DEVELOPER = "developer"


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(Enum(UserRole), default=UserRole.DEVELOPER)
    is_active = Column(Boolean, default=True)
