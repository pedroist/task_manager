from typing import Optional, List
from fastapi import Depends, HTTPException, status
from app.models.user import User as DatabaseUser, UserRole
from app.schemas.user import User, UserCreate, UserUpdate
from app.repositories.user_repository import UserRepository
from app.core.security import get_password_hash, verify_password


class UserService:
    def __init__(
        self,
        user_repository: UserRepository = Depends()
    ) -> None:
        self.repository = user_repository

    def get_by_email(self, email: str) -> Optional[User]:
        db_user = self.repository.get_by_email(email)
        return User.model_validate(db_user) if db_user else None

    def get_by_username(self, username: str) -> Optional[User]:
        db_user = self.repository.get_by_username(username)
        return User.model_validate(db_user) if db_user else None

    def get_developers(self) -> List[User]:
        db_developers = self.repository.get_users_by_role(UserRole.DEVELOPER)
        return [User.model_validate(dev) for dev in db_developers]

    def create(self, user_in: UserCreate) -> User:
        # Check if email exists
        if self.repository.get_by_email(user_in.email):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered"
            )
        # Check if username exists
        if self.repository.get_by_username(user_in.username):
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already registered"
            )
        
        hashed_password = get_password_hash(user_in.password)
        db_user = self.repository.create(user_in, hashed_password)
        return User.model_validate(db_user)

    def authenticate(self, username_or_email: str, password: str) -> Optional[DatabaseUser]:
        db_user = (
            self.repository.get_by_email(username_or_email) or 
            self.repository.get_by_username(username_or_email)
        )
        if not db_user:
            return None
        if not verify_password(password, db_user.hashed_password):
            return None
        return db_user

    def update(self, user_id: int, user_in: UserUpdate) -> User:
        db_user = self.repository.get(user_id)
        if not db_user:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="User not found"
            )
        if user_in.password:
            hashed_password = get_password_hash(user_in.password)
            user_in_data = user_in.model_dump()
            user_in_data["hashed_password"] = hashed_password
            del user_in_data["password"]
        else:
            user_in_data = user_in.model_dump(exclude={"password"})
        
        updated_db_user = self.repository.update(db_user, user_in_data)
        return User.model_validate(updated_db_user)
