"""create table votes

Revision ID: 6b2d6aa56269
Revises: a92313b627ce
Create Date: 2023-09-08 12:23:44.154110

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6b2d6aa56269'
down_revision: Union[str, None] = 'a92313b627ce'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute(f"""
    CREATE TABLE IF NOT EXISTS votes (
        eid UUID REFERENCES elections(eid) ON DELETE CASCADE,
        votevalue INT
    );
""")


def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS votes;
""")
