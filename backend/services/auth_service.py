from backend.repositories.user_repository import UserRepository
from backend.core.security import (
    create_access_token,
    create_refresh_token,
    decode_token,
    hash_password,
    verify_password
)
from backend.repositories.refresh_repository import RefreshRepository
from backend.models.refresh_token import RefreshToken
from backend.models.user import User




class AuthService:

    def __init__(self):
        self.repo = UserRepository()
        self.refresh_repo = RefreshRepository()
        

    def register(self, db, email, password):

        if self.repo.get_by_email(db, email):
            return None
        
        user = User(
            email=email,
            hashed_password=hash_password(password),
            role="user"
        )
        

        return self.repo.create(
            db, 
            user
        )


    def login(self, db, email, password):
        user = self.repo.get_by_email(db, email)

        if not user:
            return None
        
        if not verify_password(password, user.hashed_password):
            return None

        access = create_access_token({"sub": user.email, "role": user.role})
        refresh = create_refresh_token({"sub": user.email})

        self.refresh_repo.create(db, refresh, user.id)

        return {
            "access_token": access,
            "refresh_token": refresh,
            "token_type": "bearer"
        }
    
    def refresh(self, db, refresh_token: str):
        
        token_obj = self.refresh_repo.get(db, refresh_token)

        if not token_obj or token_obj.revoked:
            return None
        
        payload = decode_token(refresh_token)

        if not payload or payload.get("type") != "refresh":
            return None
        
        email = payload.get("sub")
        user = self.repo.get_by_email(db, email)

        if not user:
            return None
        
        new_access = create_access_token({
            "sub": user.email,
            "role": user.role
        })
        new_refresh = create_refresh_token({"sub": user.email})
        self.refresh_repo.revoke(
            db,
            refresh_token
        )

        self.refresh_repo.create(
            db,
            new_refresh,
            user.id
        )

        return {
            "access_token": new_access,
            "refresh_token": new_refresh,
            "token_type": "bearer"
        }