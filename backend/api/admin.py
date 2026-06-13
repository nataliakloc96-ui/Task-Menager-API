from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from backend.core.dependencies import (
    get_db,
    get_current_user
)

from backend.models.user import User


router = APIRouter()

def admin_required(current_user=Depends(get_current_user)):

    if current_user.role != "admin":
        raise HTTPException(
            status_code=403,
            detail="Admin only"
        )
    
    return current_user

@router.get("/users")
def get_users(
        db: Session = Depends(get_db),
        admin=Depends(admin_required)
):
    return db.query(User).all()