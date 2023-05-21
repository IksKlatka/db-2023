"""create table movie_genres

Revision ID: a22e8e043326
Revises: ab2b517f494a
Create Date: 2023-04-28 16:18:28.238878

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a22e8e043326'
down_revision = 'ab2b517f494a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
    CREATE TABLE movie_genres(
    movie_id int REFERENCES movies(movie_id) ON DELETE CASCADE,
    genre_id int REFERENCES genres(genre_id) ON DELETE CASCADE
    );
    """)


def downgrade() -> None:
    op.execute("""
    DROP TABLE IF EXISTS movie_genres CASCADE;
    """)