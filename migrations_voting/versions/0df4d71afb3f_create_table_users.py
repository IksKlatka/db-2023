"""create table users

Revision ID: 0df4d71afb3f
Revises: 
Create Date: 2023-09-08 12:13:19.406684

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '0df4d71afb3f'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(f"""
    CREATE TABLE IF NOT EXISTS users (
        uid UUID UNIQUE NOT NULL, 
        name TEXT UNIQUE NOT NULL
    );
""")


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS users; 
""")
