from datetime import datetime, timedelta, UTC
from jose import jwt, JWTError
from passlib.context import CryptContext
import os
from uuid import uuid4



SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret")
ALGORITHM = "HS256"

ACCESS_EXPIRE_MIN = 15
REFRESH_EXPIRE_DAYS = 7



pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def verify_password(password: str, hashed: str) -> bool:
    return pwd_context.verify(password, hashed)

def create_token(data: dict, expires_delta: timedelta, token_type: str):
    payload = data.copy()
    payload["exp"] = datetime.now(UTC) + expires_delta
    payload["type"] = token_type

    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

def create_access_token(data: dict):
    return create_token(
        data,
        timedelta(minutes=ACCESS_EXPIRE_MIN),
        "access"
    )

def create_refresh_token(data: dict):
    payload = data.copy()
    payload["exp"] = datetime.now(UTC) + timedelta(days=REFRESH_EXPIRE_DAYS)
    payload["type"] = "refresh"
    payload["jti"] = str(uuid4())


    return jwt.encode(
        payload, 
        SECRET_KEY, 
        algorithm=ALGORITHM
    )
    

def decode_token(token: str):
    try:
        return jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
    
    except JWTError:
        return None