from pydantic import BaseModel, ConfigDict
from typing import Optional
from datetime import datetime
from app.models.task import TaskStatus
from .user import UserBasic  # Import from user schema


# Shared properties
class TaskBase(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.TODO
    assignee_id: Optional[int] = None  # Keep ID for input


# Properties to receive via API on creation
class TaskCreate(TaskBase):
    title: str
    description: str


# Properties to receive via API on update
class TaskUpdate(TaskBase):
    pass


# Properties to return via API
class Task(TaskBase):
    id: int
    created_at: datetime
    updated_at: datetime
    creator: UserBasic        # Use object instead of ID
    assignee: Optional[UserBasic] = None  # Use object instead of ID
    model_config = ConfigDict(from_attributes=True)
    