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

poetry add fastapi uvicorn sqlalchemy psycopg2 alembic passlib "python-jose[cryptography]" pydantic python-dotenv pydantic-settings email-validator python-multipart bcrypt

poetry run alembic init alembic
```
After the skeleton of the project is created, we should create the postgres db:

```
psql postgres

CREATE DATABASE task_manager;
```
Verify that the db is created:

```
\l
```

Exit psql:

```
\q
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
- pydantic-settings → Settings management using Pydantic models. Allows you to:
  - Load environment variables with type validation
  - Provide default values for settings
  - Automatically parse environment variables into Python types (int, bool, etc.)
  - Nest settings models
  - Load settings from .env files, environment variables, or secrets files
- python-dotenv → Loads .env files for environment variables.
- email-validator → Provides email validation for Pydantic's EmailStr type.
- python-multipart → Enables parsing of form data, required for OAuth2 password flow.
- bcrypt → Backend for passlib, provides the actual password hashing implementation.

## Create Alembic migrations:

First we need to add the models to the alembic/env.py file:

```
from app.models.user import User
from app.models.task import Task
```

Then we can create the migration:

```
poetry run alembic revision --autogenerate -m "Create initial tables"
```

- This command tells Alembic to automatically detect your SQLAlchemy models
- It creates a migration file based on the differences between your models and the current database state
- The -m flag provides a description message for the migration

## Apply Alembic migrations

```
poetry run alembic upgrade head
```

- This command applies the latest migration to the database
- The head flag indicates that the latest revision should be applied

```
poetry run alembic revision -m "Add initial data"

```

- This command creates a new migration file with the specified message
- It's useful for adding initial data to the database

