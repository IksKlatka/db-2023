"""create table groupresource and foreign keys

Revision ID: dfb6695874cb
Revises: 635b800fb2d9
Create Date: 2023-03-28 13:51:54.307767

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dfb6695874cb'
down_revision = '635b800fb2d9'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
        --sql
        CREATE TABLE group_resource (
            groupid INT REFERENCES securitygroup(groupid),
            resourceid INT REFERENCES securedresource(resourceid),

            CONSTRAINT groupresource_pk PRIMARY KEY (groupid, resourceid)
            );
    """)


def downgrade() -> None:
    op.execute(f"""
        --sql
        DROP TABLE group_resource;
""")
