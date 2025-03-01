from typing import List, Optional
from sqlalchemy.orm import Session
from fastapi import Depends
from app.models.database_task import Task as DatabaseTask
from app.schemas.task_schema import TaskCreate, TaskUpdate
from app.db.session import get_db

class TaskRepository:
    def __init__(self, db: Session = Depends(get_db)) -> None:
        self.db = db

    def get(self, id: int) -> Optional[DatabaseTask]:
        return self.db.query(DatabaseTask).filter(DatabaseTask.id == id).first()

    def get_all(self, skip: int = 0, limit: int = 100) -> List[DatabaseTask]:
        return self.db.query(DatabaseTask).offset(skip).limit(limit).all()

    def get_user_tasks(self, user_id: int, skip: int = 0, limit: int = 100) -> List[DatabaseTask]:
        return (
            self.db.query(DatabaseTask)
            .filter(
                (DatabaseTask.creator_id == user_id) |
                (DatabaseTask.assignee_id == user_id)
            )
            .offset(skip)
            .limit(limit)
            .all()
        )

    def create(self, obj_in: TaskCreate, creator_id: int) -> DatabaseTask:
        db_obj = DatabaseTask(**obj_in.model_dump(), creator_id=creator_id)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def update(self, db_obj: DatabaseTask, obj_in: TaskUpdate) -> DatabaseTask:
        obj_data = obj_in.model_dump(exclude_unset=True)
        for field, value in obj_data.items():
            setattr(db_obj, field, value)
        self.db.add(db_obj)
        self.db.commit()
        self.db.refresh(db_obj)
        return db_obj

    def delete(self, id: int) -> None:
        obj = self.db.query(DatabaseTask).get(id)
        self.db.delete(obj)
        self.db.commit() 