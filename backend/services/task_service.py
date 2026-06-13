from sqlalchemy.orm import Session
from backend.repositories.task_repository import TaskRepository
from backend.schemas.task import TaskCreate, TaskUpdate
from backend.models.user import User

class TaskService:

    def __init__(self):
        self.repo = TaskRepository()

    def get_tasks(self, db: Session, user_id: int):
        return self.repo.get_all(
            db,
            user_id
        )
    
    def get_task(self, db: Session, task_id: int, user_id: int):
        return self.repo.get(db, task_id, user_id)
    
    def create_task(self, db: Session, task: TaskCreate):
        return self.repo.create(db, task)
    
    def update_task(self, db: Session, task_id: int, task: TaskUpdate):
        return self.repo.update(db, task_id, task)
    
    def delete_task(self, db: Session, task_id: int, user_id: int):
        return self.repo.delete(db, task_id, user_id)
    
    def get_all_users(self, db:Session):
        return db.query(User).all()