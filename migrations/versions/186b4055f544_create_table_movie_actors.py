"""

create table movie_actors

Revision ID: 186b4055f544
Creation date: 2023-04-20 18:51:10.093367

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = '186b4055f544'
down_revision = 'd9f6e618d264'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql
    CREATE TABLE movie_actors(
        credit_id   TEXT, 
        movie_id    INT,
        actor_id    INT, 
        cast_id     INT,
        character   TEXT, 
        gender      INT, 
        orders      INT,        

        CONSTRAINT fk_movie_id FOREIGN KEY (movie_id)
            REFERENCES movies(id),
        CONSTRAINT fk_actor_id FOREIGN KEY (actor_id)
            REFERENCES actors(id)            
    );
""")


def downgrade() -> None:
    op.execute(f"""
    --sql
    DROP TABLE IF EXISTS movie_actors CASCADE;
""")