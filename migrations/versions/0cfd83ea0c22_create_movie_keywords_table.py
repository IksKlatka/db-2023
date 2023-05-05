"""

create movie_keywords table

Revision ID: 0cfd83ea0c22
Creation date: 2023-04-29 12:12:34.856501

"""
from alembic import op, context


# revision identifiers, used by Alembic.
revision = '0cfd83ea0c22'
down_revision = 'de0565ec2eb9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
        CREATE TABLE movie_keywords(
            movie_id INT,
            keyword_id INT,
            
            CONSTRAINT fk_movie_id FOREIGN KEY (movie_id)
                REFERENCES movies(movie_id),
            CONSTRAINT fk_keyword_id FOREIGN KEY (keyword_id)
                REFERENCES keywords(keyword_id)  
            );
    """)

def downgrade() -> None:
    op.execute(f"""
    DROP TABLE IF EXISTS movie_keywords CASCADE; 
""")


