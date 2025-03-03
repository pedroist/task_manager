from fastapi import APIRouter
from app.api.v1.endpoints import auth, user, task

api_router = APIRouter()

# Include the auth router
api_router.include_router(auth.router, prefix="/auth", tags=["auth"])
api_router.include_router(user.router, prefix="/users", tags=["users"])
api_router.include_router(task.router, prefix="/tasks", tags=["tasks"])
