"""

create table movie_crew

Revision ID: d8ea86a9dc10
Creation date: 2023-04-20 20:33:59.345494

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = 'd8ea86a9dc10'
down_revision = 'c478838a27fe'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql
    CREATE TABLE movie_crew(
        credit_id TEXT,
        movie_id INT,
        person_id INT,
        job TEXT,
        department TEXT,
        gender INT,

        CONSTRAINT fk_movie_id FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        CONSTRAINT fk_person_id FOREIGN KEY (person_id)
            REFERENCES crew(id)      
    )

""")


def downgrade() -> None:
    op.execute(f"""
        DROP TABLE IF EXISTS movie_crew CASCADE;
    """)
