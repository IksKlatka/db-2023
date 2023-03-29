"""
inserting values into accesskey, securedresource, aecuritygroup

Revision ID: 7f30727428ad
Revises: dfb6695874cb
Create Date: 2023-03-28 15:42:08.560762

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7f30727428ad'
down_revision = 'dfb6695874cb'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
    --sql 
    
    --dodawanie kluczy, zasobu i grupy
    INSERT INTO accesskey(name) VALUES ('kone');
    INSERT INTO accesskey(name) VALUES ('ktwo');
    INSERT INTO securedresource(name) VALUES ('rone');
    INSERT INTO securitygroup(groupname) VALUES ('gone'); 
    
    --stworzenie polaczen 
    INSERT INTO group_resource (groupid, resourceid) VALUES (1, 1);
    INSERT INTO group_key (groupid, keyid) VALUES (1, 1);
    INSERT INTO group_key (groupid, keyid) VALUES (1, 2);
    
""")


def downgrade() -> None:
    op.execute(f"""
    --sql 
    
    -- usuniecie polaczen 
    DELETE FROM group_key WHERE groupid=1;
    DELETE FROM group_resource WHERE groupid=1;
    
    -- usuniecie pozostalych rekordow
    DELETE FROM accesskey WHERE keyid=1;
    DELETE FROM accesskey WHERE keyid=2;
    DELETE FROM securedresource WHERE resourceid=1;
    DELETE FROM securitygroup WHERE groupid=1;
""")
