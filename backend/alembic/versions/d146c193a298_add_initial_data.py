"""Add initial data

Revision ID: d146c193a298
Revises: 7641e6d903fd
Create Date: 2025-03-03 14:41:33.229483

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from app.core.security import get_password_hash


# revision identifiers, used by Alembic.
revision: str = 'd146c193a298'
down_revision: Union[str, None] = '7641e6d903fd'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Add manager
    manager_password = get_password_hash('manager123')
    op.execute(f"""
        INSERT INTO users (email, username, hashed_password, role, is_active)
        VALUES ('manager@example.com', 'manager', '{manager_password}', 'MANAGER', true)
    """)

    # Add developers
    dev1_password = get_password_hash('dev1pass')
    dev2_password = get_password_hash('dev2pass')
    op.execute(f"""
        INSERT INTO users (email, username, hashed_password, role, is_active)
        VALUES 
        ('dev1@example.com', 'developer1', '{dev1_password}', 'DEVELOPER', true),
        ('dev2@example.com', 'developer2', '{dev2_password}', 'DEVELOPER', true)
    """)

    # Add tasks
    op.execute("""
        INSERT INTO tasks (title, description, status, creator_id, assignee_id)
        VALUES 
        ('Setup Project Structure', 'Create initial project structure and configure dependencies', 'TODO', 1, 2),
        ('Implement User Authentication', 'Add JWT authentication and user registration', 'IN_PROGRESS', 1, 2),
        ('Create Task API', 'Implement CRUD operations for tasks', 'TODO', 1, 3),
        ('Write API Documentation', 'Document all API endpoints using OpenAPI', 'TODO', 1, NULL),
        ('Setup CI/CD Pipeline', 'Configure GitHub Actions for automated testing and deployment', 'TODO', 1, NULL)
    """)


def downgrade() -> None:
    # Remove all data in reverse order
    op.execute("DELETE FROM tasks")
    op.execute("DELETE FROM users")
