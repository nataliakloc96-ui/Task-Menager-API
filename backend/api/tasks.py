from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from backend.models.task import Task 
from backend.core.dependencies import (
    get_db,
    get_current_user,
    require_admin
) 
from backend.core.database import SessionLocal 
from backend.schemas.task import TaskCreate, TaskOut, TaskUpdate 
from backend.services.task_service import TaskService 


router = APIRouter()
service = TaskService()



def get_admin_user(
        current_user = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(status_code=403, detail="Access denied")
    return current_user


@router.get("/", response_model=list[TaskOut])
def get_tasks(
    status: str | None = Query(None),
    search: str | None = None,
    sort: str | None = None,
    skip: int = 0,
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
    
):
    query = db.query(Task).filter(
        Task.owner_id == current_user.id
    )

    if status:
        query = query.filter(Task.status == status)
    
    if search: 
        query = query.filter(
            Task.title.ilike(f"%{search}%")
        )
    
    if sort == "priority":
        query = query.order_by(Task.priority)

    elif sort == "created":
        query = query.order_by(Task.created_at.desc())

    elif sort == "due_date":
        query = query.order_by(Task.due_date)
    
    

    return query.offset(skip).limit(limit).all()
    
    

@router.post("/", response_model=TaskOut)
def create_task(task: TaskCreate, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    new_task = Task(
        title=task.title, 
        due_date=task.due_date,
        priority=task.priority,
        owner_id=current_user.id
    )  

    db.add(new_task)
    db.commit()
    db.refresh(new_task)

    return new_task

@router.get("/{task_id}", response_model = TaskOut)
def get_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    task = db.query(Task).filter(Task.id == task_id, Task.owner_id == current_user.id).first()
    if not task: 
        raise HTTPException(status_code=404, detail="Task not found")
    return task

@router.delete("/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db), current_user: str = Depends(get_current_user)):
    deleted = service.delete_task(db, task_id, current_user.id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Task not found")
    return {"message": "deleted"}

@router.get("/admin/users")
def get_users(
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    return service.get_all_users(db)

@router.put("/{task_id}", response_model=TaskOut)
def update_task(
    task_id: int,
    data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.owner_id == current_user.id
        )
        .first()
    )

    if not task:
        raise HTTPException(
            status_code=404,
            detail="Task not found"
        )
    
    if data.title is not None:
        task.title = data.title

    if data.status is not None:
        task.status = data.status
    
    if data.priority is not None:
        task.priority = data.priority
    
    if data.due_date is not None:
        task.due_date = data.due_date

    db.commit()
    db.refresh(task)

    return task


