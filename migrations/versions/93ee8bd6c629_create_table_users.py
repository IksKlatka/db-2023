"""create table users

Revision ID: 93ee8bd6c629
Revises: 7f30727428ad
Create Date: 2023-03-29 11:06:17.486951

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '93ee8bd6c629'
down_revision = '7f30727428ad'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql 
    
    CREATE TABLE users (
        uuid UUID DEFAULT gen_random_uuid() PRIMARY KEY,
        username TEXT NOT NULL,
        password TEXT NOT NULL,
        created_at TIMESTAMP WITH TIME ZONE NOT NULL,
        updated_at TIMESTAMP WITH TIME ZONE
        );

""")

def downgrade() -> None:
    op.execute(f"""
    --sql
    
    DROP TABLE users;
    
""")