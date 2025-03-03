from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from app.schemas.user import User, UserUpdate
from app.models.user import User as DatabaseUser, UserRole
from app.services.user_service import UserService
from app.api import deps

router = APIRouter()


@router.get("/me", response_model=User)
def get_current_user_info(
    db_current_user: DatabaseUser = Depends(deps.get_current_user)
) -> User:
    """Get current user information"""
    return User.model_validate(db_current_user)


@router.put("/me", response_model=User)
def update_current_user(
    *,
    user_in: UserUpdate,
    user_service: UserService = Depends(),
    db_current_user: DatabaseUser = Depends(deps.get_current_user)
) -> User:
    return user_service.update(db_current_user.id, user_in)


@router.get("/developers", response_model=List[User])
def get_developers(
    service: UserService = Depends(),
    db_current_user: DatabaseUser = Depends(deps.get_current_user)
) -> List[User]:
    """Get all developers (only accessible by managers)"""
    if db_current_user.role != UserRole.MANAGER:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Not enough permissions"
        )
    return service.get_developers()
