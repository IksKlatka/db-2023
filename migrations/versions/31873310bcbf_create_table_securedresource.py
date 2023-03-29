"""create table securedresource

Revision ID: 31873310bcbf
Revises: 26371eff3dfc
Create Date: 2023-03-28 13:36:45.090490

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '31873310bcbf'
down_revision = '26371eff3dfc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql
    CREATE TABLE securedresource (
	resourceid SERIAL PRIMARY KEY,
	name TEXT NOT NULL UNIQUE,
	isopen BOOL DEFAULT TRUE NOT NULL
);
""")


def downgrade() -> None:
    op.execute(f"""
    --sql
    DROP TABLE securedresource;
""")
