from typing import Optional, List
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.user import User as DatabaseUser, UserRole
from app.schemas.user import UserCreate
from app.db.session import get_db


class UserRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get_by_email(self, email: str) -> Optional[DatabaseUser]:
        return self.db.query(DatabaseUser).filter(DatabaseUser.email == email).first()

    def get_by_username(self, username: str) -> Optional[DatabaseUser]:
        return self.db.query(DatabaseUser).filter(DatabaseUser.username == username).first()

    def get_users_by_role(self, role: UserRole) -> List[DatabaseUser]:
        return self.db.query(DatabaseUser).filter(DatabaseUser.role == role).all()

    def create(self, user_in: UserCreate, hashed_password: str) -> DatabaseUser:
        db_user = DatabaseUser(
            email=user_in.email,
            username=user_in.username,
            hashed_password=hashed_password,
            role=user_in.role
        )
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user

    def get(self, id: int) -> Optional[DatabaseUser]:
        return self.db.query(DatabaseUser).filter(DatabaseUser.id == id).first()

    def update(self, db_user: DatabaseUser, obj_data: dict) -> DatabaseUser:
        for field, value in obj_data.items():
            setattr(db_user, field, value)
        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)
        return db_user
