"""add status column to tasks

Revision ID: 6342e6583201
Revises: 
Create Date: 2026-01-27 15:25:39.366303

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql


# revision identifiers, used by Alembic.
revision: str = '6342e6583201'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # Create the ENUM type
    task_status_enum = postgresql.ENUM('pending', 'completed', name='task_status')
    task_status_enum.create(op.get_bind(), checkfirst=True)

    # Add the status column
    op.add_column(
        'Tasks',
        sa.Column(
            'status',
            task_status_enum,
            server_default='pending',
            nullable=False
        )
    )

def downgrade() -> None:
    # Remove the column first
    op.drop_column('Tasks', 'status')

    # Drop the ENUM type
    task_status_enum = postgresql.ENUM('pending', 'completed', name='task_status')
    task_status_enum.drop(op.get_bind(), checkfirst=True)
