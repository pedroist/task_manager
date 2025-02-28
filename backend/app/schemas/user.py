from pydantic import BaseModel, EmailStr, ConfigDict
from typing import Optional
from app.models.user import UserRole


class UserBasic(BaseModel):
    id: int
    username: str
    model_config = ConfigDict(from_attributes=True)


# Shared properties
class UserBase(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    is_active: Optional[bool] = True
    role: Optional[UserRole] = UserRole.DEVELOPER


# Properties to receive via API on creation
class UserCreate(UserBase):
    email: EmailStr
    username: str
    password: str


# Properties to receive via API on update
class UserUpdate(UserBase):
    password: Optional[str] = None


# Properties to return via API
class User(UserBase):
    id: int
    model_config = ConfigDict(from_attributes=True)
