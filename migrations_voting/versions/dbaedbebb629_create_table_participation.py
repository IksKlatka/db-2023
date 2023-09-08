"""create table participation

Revision ID: dbaedbebb629
Revises: fdbe13c4f236
Create Date: 2023-09-08 12:18:04.884333

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dbaedbebb629'
down_revision: Union[str, None] = 'fdbe13c4f236'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(f"""
    CREATE TABLE IF NOT EXISTS participation (
        uid UUID REFERENCES users(uid) ON DELETE CASCADE,
        eid UUID REFERENCES elections(eid) ON DELETE CASCADE
    );
""")


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS participation;
""")
