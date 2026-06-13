# Task Manager API

![Tests](https://github.com/nataliakloc96-ui/Task-Menager-API/actions/workflows/tests.yml/badge.svg)

Production-style REST API for task management built with FastAPI.

The project demonstrates backend architecture, authentication, authorization, testing, Docker environment and CI pipeline.

---

## Tech Stack

### Backend
- Python 3.11
- FastAPI
- SQLAlchemy ORM
- Pydantic v2
- PostgreSQL
- Redis
- Alembic

### Security
- JWT Authentication
- Access & Refresh Tokens
- Password hashing (bcrypt)
- Token blacklist
- Role Based Access Control (RBAC)
- User permissions

### DevOps & Quality
- Docker
- Docker Compose
- GitHub Actions CI
- Pytest
- Structured JSON logging
- Request tracing

---

# Architecture
Client

↓

FastAPI Router

↓

Service Layer

↓

Repository Layer

↓

PostgreSQL

---

# Project structure:


backend/

├── api/
│ ├── auth.py
│ ├── tasks.py
│ └── admin.py
│

├── core/
│ ├── database.py
│ ├── security.py
│ ├── redis.py
│ └── logger.py
│

├── middleware/
│ └── logging.py
│

├── models/
│

├── repositories/
│

├── services/
│

└── tests/

--- 

# Authentication

The API uses JWT authentication.

Login returns:

```json
{
  "access_token": "...",
  "refresh_token": "...",
  "token_type": "bearer"
}

Access tokens protect private routes.

Refresh tokens allow creating new access tokens.

---

## RBAC Authorization

Admin endpoints are protected:

Example:

GET /admin/users

Permissions:

User	        Result
Anonymous	    401 Unauthorized
User	        403 Forbidden
Admin	        200 OK

--- 

## API Endpoints

# Auth

Method	        Endpoint
POST	        /auth/register
POST	        /auth/login
POST	        /auth/refresh

# Tasks
Method	        Endpoint
GET	            /tasks
GET	            /tasks/{id}
POST	        /tasks
PUT	            /tasks/{id}
DELETE	        /tasks/{id}

# Admin
Method	        Endpoint
GET	            /admin/users

---

## Docker

Start application:

docker compose up --build


Services:

API → port 8000
PostgreSQL → port 5432
Redis → port 6379

Swagger:

http://localhost:8000/docs

---

## Database migrations

Create migration:

alembic revision --autogenerate -m "message"

Run migrations:

alembic upgrade head

---

## Tests

Run:

pytest -vv


Current status:

12 passed

Tests include:

Authentication
JWT flow
Refresh tokens
CRUD operations
Permissions
Admin RBAC

---

## CI/CD

GitHub Actions automatically:

installs dependencies
prepares environment
runs tests

Pipeline status is visible at the top of README.

---

## Features

✔ Clean Architecture
✔ Repository Pattern
✔ Dependency Injection
✔ JWT Security
✔ RBAC
✔ Dockerized Environment
✔ CI Pipeline
✔ Automated Tests
✔ Structured Logging