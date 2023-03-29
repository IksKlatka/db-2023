"""create table groupkey and foreign keys

Revision ID: 635b800fb2d9
Revises: 31873310bcbf
Create Date: 2023-03-28 13:39:42.613697

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '635b800fb2d9'
down_revision = '31873310bcbf'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql
    CREATE TABLE group_key (
        groupid INT REFERENCES securitygroup(groupid),
        keyid INT REFERENCES accesskey(keyid),

        CONSTRAINT groupkey_pk PRIMARY KEY (groupid, keyid)
        );
""")

def downgrade() -> None:
    op.execute(f"""
    --sql
    DROP TABLE group_key;
""")
