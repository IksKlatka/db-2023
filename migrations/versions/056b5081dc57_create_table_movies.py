"""

create table movies

Revision ID: 056b5081dc57
Creation date: 2023-04-20 18:49:57.881483

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = '056b5081dc57'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql 
    CREATE TABLE movies(
        id SERIAL PRIMARY KEY,
        title TEXT
    );
""")


def downgrade() -> None:
    op.execute(f"""
    --sql 
    DROP TABLE IF EXISTS movies CASCADE;
""")



def seed() -> None:
    seeds = []

    for seed in seeds:
        pass
