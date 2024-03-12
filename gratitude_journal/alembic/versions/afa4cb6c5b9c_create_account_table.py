"""create account table

Revision ID: afa4cb6c5b9c
Revises: 
Create Date: 2024-03-11 23:19:24.906551

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
import uuid
from datetime import datetime

# revision identifiers, used by Alembic.
revision: str = 'afa4cb6c5b9c'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'users',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('unique_id', sa.String(), nullable=False, default=str(uuid.uuid4)),
        sa.Column('username', sa.String(), unique=True),
        sa.Column('email', sa.String(), unique=True, nullable=False),
        sa.Column('hashed_password', sa.String()),
        sa.Column('full_name', sa.String(), nullable=False),
        sa.Column('timestamp', sa.DateTime(), default=datetime.now),
        sa.PrimaryKeyConstraint('id')
    )


def downgrade() -> None:
    op.drop_table('users')
