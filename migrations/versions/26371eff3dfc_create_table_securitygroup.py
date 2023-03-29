"""create table securitygroup

Revision ID: 26371eff3dfc
Revises: 44dc196c6ac9
Create Date: 2023-03-28 12:42:24.516265

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '26371eff3dfc'
down_revision = '44dc196c6ac9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql
    CREATE TABLE securitygroup(
        groupid SERIAL PRIMARY KEY,
        groupname TEXT NOT NULL UNIQUE
        );
""")


def downgrade() -> None:
    op.execute(f"""
    --sql
    DROP TABLE securitygroup;
""")
