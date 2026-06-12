from backend.core.database import Base, engine
from backend.models.user import User
from backend.models.task import Task
from backend.models.refresh_token import RefreshToken

def init_db():
    Base.metadata.create_all(bind=engine)