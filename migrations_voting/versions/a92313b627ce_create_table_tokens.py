"""create table tokens

Revision ID: a92313b627ce
Revises: dbaedbebb629
Create Date: 2023-09-08 12:22:31.530018

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a92313b627ce'
down_revision: Union[str, None] = 'dbaedbebb629'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(f"""
    CREATE TABLE IF NOT EXISTS tokens (
        eid UUID REFERENCES elections(eid) ON DELETE CASCADE,
        tokenid UUID NOT NULL UNIQUE
    );
""")


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS tokens;
""")
