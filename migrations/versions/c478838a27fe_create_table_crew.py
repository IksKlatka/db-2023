"""

create table crew

Revision ID: c478838a27fe
Creation date: 2023-04-20 20:33:01.548657

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'c478838a27fe'
down_revision = '186b4055f544'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql 
    CREATE TABLE crew(
        id SERIAL PRIMARY KEY,
        name TEXT
    );
""")


def downgrade() -> None:
    op.execute(f"""
    --sql 
    DROP TABLE IF EXISTS crew CASCADE;
""")