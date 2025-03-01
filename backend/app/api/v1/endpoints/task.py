from typing import List
from fastapi import APIRouter, Depends, status
from app.schemas import Task, TaskCreate, TaskUpdate
from app.models.user import User
from app.services.task_service import TaskService
from app.api import deps

router = APIRouter()


@router.get("/", response_model=List[Task])
def get_tasks(
    service: TaskService = Depends(),
    db_current_user: User = Depends(deps.get_current_user),
    skip: int = 0,
    limit: int = 100
) -> List[Task]:
    return service.get_tasks(db_current_user, skip=skip, limit=limit)


@router.post("/", response_model=Task)
def create_task(
    *,
    task_in: TaskCreate,
    service: TaskService = Depends(),
    db_current_user: User = Depends(deps.get_current_user)
) -> Task:
    return service.create_task(task_in, db_current_user)


@router.get("/{task_id}", response_model=Task)
def get_task(
    *,
    task_id: int,
    service: TaskService = Depends(),
    db_current_user: User = Depends(deps.get_current_user)
) -> Task:
    return service.get_task(task_id, db_current_user)


@router.put("/{task_id}", response_model=Task)
def update_task(
    *,
    task_id: int,
    task_in: TaskUpdate,
    service: TaskService = Depends(),
    db_current_user: User = Depends(deps.get_current_user)
) -> Task:
    return service.update_task(task_id, task_in, db_current_user)


@router.delete("/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    *,
    task_id: int,
    service: TaskService = Depends(),
    db_current_user: User = Depends(deps.get_current_user)
) -> None:
    service.delete_task(task_id, db_current_user)
