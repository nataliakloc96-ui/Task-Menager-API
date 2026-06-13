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

The project follows a layered architecture pattern with separation of responsibilities.

```text
Client
  |
  v
FastAPI Router
  |
  v
Service Layer
  |
  v
Repository Layer
  |
  v
PostgreSQL
```

Additional components:

- Redis → rate limiting and token blacklist
- Middleware → request logging and tracing
- GitHub Actions → automated testing

📌 Detailed architecture diagram:

[View architecture](docs/architecture.md)
---

# Project structure:

```
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
```
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
```

Access tokens protect private routes.

Refresh tokens allow creating new access tokens.

---

# RBAC Authorization

Admin endpoints are protected:

Example:

``` GET /admin/users ```

Permissions:
```
User	        Result
Anonymous	    401 Unauthorized
User	        403 Forbidden
Admin	        200 OK
```
--- 

# API Endpoints

## Auth
```
<<<<<<< HEAD
Method	       Endpoint
=======
Method	        Endpoint
>>>>>>> eadbf54 (Add architecture documentation)
POST	        /auth/register
POST	        /auth/login
POST	        /auth/refresh
```
<<<<<<< HEAD
=======

>>>>>>> eadbf54 (Add architecture documentation)
## Tasks
```
Method	        Endpoint
GET	            /tasks
GET	            /tasks/{id}
POST	          /tasks
PUT	            /tasks/{id}
DELETE	        /tasks/{id}
```
<<<<<<< HEAD
=======

>>>>>>> eadbf54 (Add architecture documentation)
## Admin
```
Method	        Endpoint
GET	            /admin/users
```
<<<<<<< HEAD
=======

>>>>>>> eadbf54 (Add architecture documentation)
---

# Docker

Start application:

``` docker compose up --build ```


Services:
```
API → port 8000
PostgreSQL → port 5432
Redis → port 6379
```
<<<<<<< HEAD
=======

>>>>>>> eadbf54 (Add architecture documentation)
Swagger:

``` http://localhost:8000/docs ```

---

# Database migrations

Create migration:

``` alembic revision --autogenerate -m "message" ```

Run migrations:

``` alembic upgrade head ```

---

# Tests

Run:

```pytest -vv```


## Current status:
```
12 passed
```
## Tests include:
```
Authentication
JWT flow
Refresh tokens
CRUD operations
Permissions
Admin RBAC
```
---

# CI/CD

## GitHub Actions automatically:
```
installs dependencies
prepares environment
runs tests
```
Pipeline status is visible at the top of README.

---

# Features
```
✔ Clean Architecture
✔ Repository Pattern
✔ Dependency Injection
✔ JWT Security
✔ RBAC
✔ Dockerized Environment
✔ CI Pipeline
✔ Automated Tests
✔ Structured Logging
```
<<<<<<< HEAD
=======
---

# What I learned

During this project I practiced:

## Backend Development

- designing REST API with FastAPI
- creating layered backend architecture
- separating API, service and repository logic
- working with dependency injection


## Database

- designing relational database models
- using SQLAlchemy ORM
- managing schema changes with Alembic migrations


## Security

- implementing JWT authentication
- access and refresh token flow
- password hashing
- role based access control
- protecting user resources


## Testing

- writing automated tests with pytest
- mocking external dependencies
- testing authentication flows
- testing permissions


## DevOps

- containerizing applications with Docker
- managing services with Docker Compose
- creating CI pipelines with GitHub Actions
>>>>>>> eadbf54 (Add architecture documentation)
