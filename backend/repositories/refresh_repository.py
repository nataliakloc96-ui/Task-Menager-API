from backend.models.refresh_token import RefreshToken


class RefreshRepository:

    def create(self, db, token: str, user_id: int):
        obj = RefreshToken(token=token, user_id=user_id, revoked=False)
        db.add(obj)
        db.commit()
        db.refresh(obj)
        return obj
    
    def get(self, db, token: str):
        return (db.query(RefreshToken).filter(
            RefreshToken.token == token)
        .first()
        )
    def revoke(self, db, token: str):
        obj = self.get(db, token)

        if obj:
            obj.revoked = True
            db.commit()
    
    def save(self, db, token, user_id):
        refresh = RefreshToken(
            token=token,
            user_id=user_id,
            revoked=False
        )
        db.add(refresh)
        db.commit()
        db.refresh(refresh)
        return refresh
