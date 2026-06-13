from fastapi import FastAPI
from backend.api import tasks, auth, admin
from backend.middleware.logging import LoggingMiddleware

app = FastAPI()

app.add_middleware(
    LoggingMiddleware
)

app.include_router(
    auth.router,
    prefix="/auth",
    tags=["auth"]
)

app.include_router(
    admin.router,
    prefix="/admin",
    tags=["admin"]
)




app.include_router(tasks.router, prefix="/tasks", tags=["tasks"])