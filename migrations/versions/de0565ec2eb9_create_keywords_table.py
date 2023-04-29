"""

create keywords table

Revision ID: de0565ec2eb9
Creation date: 2023-04-29 12:10:52.477714

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'de0565ec2eb9'
down_revision = 'a22e8e043326'
branch_labels = None
depends_on = None


def upgrade() -> None:

    op.execute(f"""
    CREATE TABLE keywords(
        keyword_id INT SERIAL PRIMARY KEY UNIQUE NOT NULL,
        name TEXT        
        );
""")

def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS keywords CASCADE;
""")

