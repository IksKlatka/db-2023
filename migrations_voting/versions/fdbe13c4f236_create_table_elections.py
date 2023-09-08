"""create table elections

Revision ID: fdbe13c4f236
Revises: 0df4d71afb3f
Create Date: 2023-09-08 12:16:56.398656

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'fdbe13c4f236'
down_revision: Union[str, None] = '0df4d71afb3f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(f"""
    CREATE TABLE IF NOT EXISTS elections (
        eid UUID UNIQUE NOT NULL,
        name TEXT UNIQUE NOT NULL
    );
""")


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS elections;
""")
