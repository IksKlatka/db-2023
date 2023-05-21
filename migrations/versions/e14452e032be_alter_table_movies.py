"""

alter table movies

Revision ID: e14452e032be
Creation date: 2023-05-21 10:45:03.601836

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'e14452e032be'
down_revision = '0cfd83ea0c22'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
     ALTER TABLE movies
        ADD COLUMN budget int,
        ADD COLUMN popularity float,
        ADD COLUMN release_date date,
        ADD COLUMN revenue int;
     """)


def downgrade() -> None:
    op.execute("""
    ALTER TABLE movies
        DROP COLUMN budget,
        DROP COLUMN popularity,
        DROP COLUMN release_date,
        DROP COLUMN revenue;
    """)
