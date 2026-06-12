from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


from backend.core.dependencies import get_db, get_current_user, rate_limit_dependency
from backend.schemas.auth import RegisterRequest
from backend.services.auth_service import AuthService
from backend.schemas.token import TokenPair, RefreshRequest
from backend.core.security_blacklist import blacklist_token

from backend.core.security import decode_token
import time


router = APIRouter()

service = AuthService()


@router.post("/register")
def register(data: RegisterRequest, db: Session = Depends(get_db)):
    user = service.register(db, data.email, data.password)
    
    if not user:
        raise HTTPException(
            status_code=409,
            detail="User with this email already exists"
        )
    
    return {
        "id": user.id,
        "email": user.email
    }

  
@router.post("/login", summary="User login")
def login(data: OAuth2PasswordRequestForm = Depends(), _: None = Depends(rate_limit_dependency), db: Session = Depends(get_db)):
    tokens = service.login(
        db,
        data.username,
        data.password
    )
    if not tokens:
        raise HTTPException(
            status_code=401,
            detail="Invalid credentials"
        )
    

    return tokens
    

@router.post("/refresh", response_model=TokenPair)
def refresh(data: RefreshRequest, db: Session = Depends(get_db)):
    tokens = service.refresh(db, data.refresh_token)

    if not tokens:
        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token"
        )
    
    return tokens

@router.post("/me")
def me(current_user=Depends(get_current_user)):
    return {
        "id": current_user.id,
        "email": current_user.email,
        "role": current_user.role
    }

@router.post("/logout")
def logout(token: str, db: Session = Depends(get_db)):
    payload = decode_token(token)

    exp = payload["exp"] - int(time.time())

    blacklist_token(token, exp)

    return {"message": "logged out"}