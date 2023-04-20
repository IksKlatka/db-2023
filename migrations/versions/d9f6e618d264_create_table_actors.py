"""

create table actors

Revision ID: d9f6e618d264
Creation date: 2023-04-20 18:50:39.835841

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'd9f6e618d264'
down_revision = '056b5081dc57'
branch_labels = None
depends_on = None



def upgrade() -> None:
    op.execute(f"""
    --sql 
    CREATE TABLE actors(
        id SERIAL PRIMARY KEY,
        name TEXT
    );
""")


def downgrade() -> None:
    op.execute(f"""
    --sql
    DROP TABLE IF EXISTS actors CASCADE;
""")
