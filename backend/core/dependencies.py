from fastapi import Depends, HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


from backend.core.database import SessionLocal
from backend.core.security import decode_token
from backend.repositories.user_repository import UserRepository
from backend.core.security_blacklist import is_blacklisted
from backend.core.rate_limit import rate_limit


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)):
    payload = decode_token(token)

    if not payload:
        raise HTTPException(status_code=401, detail="Invalid token")
    
    if payload.get("type") != "access":
        raise HTTPException(
            status_code=401,
            detail="Invalid token type"
        )
    
    email = payload.get("sub")

    user = UserRepository().get_by_email(db, email)
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    return user

def require_admin(role: str):
    def wrapper(user=Depends(get_current_user)):
        if user.role != role:
            raise HTTPException(status_code=403, detail="Forbidden")
        return user
    return wrapper

def verify_token_not_blacklisted(token: str):
    if is_blacklisted(token):
        raise HTTPException(status_code=401, detail="Token revoked")
    
def rate_limit_dependency(request: Request):
    ip = request.client.host
    rate_limit(ip)
    