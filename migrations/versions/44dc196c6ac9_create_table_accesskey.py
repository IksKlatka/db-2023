"""create table accesskey

Revision ID: 44dc196c6ac9
Revises: 
Create Date: 2023-03-28 12:30:21.904104

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '44dc196c6ac9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql
    CREATE TABLE accesskey (
        keyid SERIAL PRIMARY KEY,
        name TEXT UNIQUE NOT NULL
        );
    """)


def downgrade() -> None:
    op.execute(f"""
    --sql
    DROP TABLE accesskey;
""")
