from sqlalchemy.orm import Session
from backend.models.task import Task
from backend.schemas.task import TaskCreate, TaskUpdate

class TaskRepository:

    def get_all(self, db: Session):
        return db.query(Task).all()
    
    def get(self, db:Session, task_id:int):
        return db.query(Task).filter(Task.id == task_id).first()
    
    def create(self, db: Session, task: TaskCreate):
        db_task = Task(**task.model_dump())
        db.add(db_task)
        db.commit()
        db.refresh(db_task)
        return db_task
    
    def update(self, db: Session, task_id: int, task: TaskUpdate):
        db_task = self.get(db, task_id)
        if not db_task:
            return None
        
        for key, value in task.model_dump(exclude_unset=True).items():
            setattr(db_task, key, value)

        
        db.commit()
        db.refresh(db_task)
        return db_task

    def delete(self, db: Session, task_id: int, user_id: int):
        db_task = (
            db.query(Task)
            .filter(Task.id == task_id, Task.owner_id == user_id)
            .first()
        )
        if not db_task:
            return False
        
        db.delete(db_task)
        db.commit()
        return True