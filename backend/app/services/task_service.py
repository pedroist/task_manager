from typing import List
from fastapi import Depends, HTTPException, status
from app.models.database_task import Task as DatabaseTask
from app.models.database_user import User as DatabaseUser, UserRole
from app.schemas.task_schema import Task, TaskCreate, TaskUpdate
from app.repositories.task_repository import TaskRepository

class TaskService:
    def __init__(
        self,
        task_repository: TaskRepository = Depends()
    ) -> None:
        self.repository = task_repository

    def get_tasks(self, db_current_user: DatabaseUser, skip: int = 0, limit: int = 100) -> List[Task]:
        if db_current_user.role == UserRole.MANAGER:
            db_tasks = self.repository.get_all(skip=skip, limit=limit)
        else:
            db_tasks = self.repository.get_user_tasks(db_current_user.id, skip=skip, limit=limit)
        return [Task.model_validate(db_task) for db_task in db_tasks]

    def create_task(self, task_in: TaskCreate, db_current_user: DatabaseUser) -> Task:
        db_task = self.repository.create(task_in, db_current_user.id)
        return Task.model_validate(db_task)

    def get_task(self, task_id: int, db_current_user: DatabaseUser) -> Task:
        db_task = self.repository.get(task_id)
        if not db_task:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Task not found"
            )
        if (db_current_user.role != UserRole.MANAGER and 
            db_current_user.id not in [db_task.creator_id, db_task.assignee_id]):
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        return Task.model_validate(db_task)

    def update_task(self, task_id: int, task_in: TaskUpdate, db_current_user: DatabaseUser) -> Task:
        db_task = self.get_task(task_id, db_current_user)
        updated_db_task = self.repository.update(db_task, task_in)
        return Task.model_validate(updated_db_task)

    def delete_task(self, task_id: int, db_current_user: DatabaseUser) -> None:
        task = self.get_task(task_id, db_current_user)
        if db_current_user.role != UserRole.MANAGER and db_current_user.id != task.creator_id:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="Not enough permissions"
            )
        self.repository.delete(task_id) 