# Team Task Management API

A FastAPI-based backend service for managing tasks within small teams. This API provides endpoints for creating, reading, updating, and deleting tasks, as well as managing team members and task assignments.

## 🚀 Features

- User authentication and authorization
- Task management (CRUD operations)
- Team member management
- Task assignment and status tracking
- Real-time task updates
- Database migrations using Alembic

## 🛠 Tech Stack

- **FastAPI**: Modern, fast web framework for building APIs with Python
- **SQLAlchemy**: SQL toolkit and ORM
- **Alembic**: Database migration tool
- **PostgreSQL**: Primary database
- **Pydantic**: Data validation using Python type annotations
- **JWT**: For secure authentication

## Commands used to create the project

```
poetry init

poetry add fastapi uvicorn sqlalchemy psycopg2 alembic passlib "python-jose[cryptography]" pydantic python-dotenv

poetry run alembic init alembic
```

## Explanation of Dependencies
- fastapi → The main web framework.
- uvicorn → ASGI server to run FastAPI.
- sqlalchemy → ORM for database models.
- psycopg2 → PostgreSQL database adapter.
- alembic → Database migrations.
- passlib → For password hashing.
- python-jose[cryptography] → For JWT authentication.
- pydantic → Data validation and serialization.
- python-dotenv → Loads .env files for environment variables.