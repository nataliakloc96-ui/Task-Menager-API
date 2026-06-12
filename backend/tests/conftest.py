import os

os.environ["TESTING"] = "True"
os.environ["DATABASE_URL"] = "sqlite:///./test.db"

import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from fastapi.testclient import TestClient
from unittest.mock import MagicMock

from backend.models.user import User
from backend.models.task import Task
from backend.models.refresh_token import RefreshToken

from backend.main import app


from backend.core.database import Base
from backend.core.dependencies import get_db

from unittest.mock import MagicMock




import backend.core.redis as redis_module




fake_redis = MagicMock()
fake_redis.get.return_value = None
fake_redis.setex.return_value = True
fake_redis.delete.return_value = 1
fake_redis.incr.return_value = 1
fake_redis.expire.return_value = True


redis_module.redis_client = fake_redis

import backend.core.redis
import backend.core.security_blacklist

backend.core.redis.redis_client = fake_redis
backend.core.security_blacklist.redis_client = fake_redis


TEST_DATABASE_URL = "sqlite:///./test.db"




engine = create_engine(
    TEST_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

TestSessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)

@pytest.fixture(scope="session", autouse=True)
def cleos_db():
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)

    yield

    Base.metadata.drop_all(bind=engine)
    
def setup_db():
    Base.metadata.create_all(bind=engine)
    yield
    Base.metadata.drop_all(bind=engine)

def override_get_db():
    db = TestSessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db


@pytest.fixture
def client():
    return TestClient(app)