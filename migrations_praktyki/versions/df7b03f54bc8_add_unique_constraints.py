"""

add unique constraints

Revision ID: df7b03f54bc8
Creation date: 2023-09-16 15:58:58.697402

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'df7b03f54bc8'
down_revision = 'cfda7936c3f2'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute(f"""
        ALTER TABLE applications 
        ADD CONSTRAINT uniq_framework_agreement UNIQUE (framework_agreement_id);
        
        ALTER TABLE ecdsa_keys 
        ADD CONSTRAINT uniq_key UNIQUE (key);

        ALTER TABLE days 
        ADD CONSTRAINT uniq_period_and_date UNIQUE (period_id, date_at);

        ALTER TABLE internship_agreements 
        ADD CONSTRAINT uniq_application_id UNIQUE (application_id);
        
        ALTER TABLE internships 
        ADD CONSTRAINT uniq_student_id UNIQUE (student_id);

        ALTER TABLE persons 
        ADD CONSTRAINT uniq_company_and_uid_in_company UNIQUE (company_id, uid_in_company);
        
        ALTER TABLE period_final_reports 
        ADD CONSTRAINT uniq_person UNIQUE (period_id);

        ALTER TABLE signature_texts 
        ADD CONSTRAINT uniq_sig_txt_document_and_person UNIQUE (document_id, person_id);
        
        ALTER TABLE signatures 
        ADD CONSTRAINT uniq_sig_document_and_person UNIQUE (document_id, person_id);

        ALTER TABLE survey 
        ADD CONSTRAINT uniq_internship_period UNIQUE (internship_period_id);

""")


def downgrade() -> None:
    op.execute(f"""
    ALTER TABLE applications 
    DROP CONSTRAINT uniq_framework_agreement;
    
    ALTER TABLE ecdsa_keys 
    DROP CONSTRAINT uniq_key;
    
    ALTER TABLE days 
    DROP CONSTRAINT uniq_period_and_date;
    
    ALTER TABLE internship_agreements 
    DROP CONSTRAINT uniq_application_id;
    
    ALTER TABLE internships 
    DROP CONSTRAINT uniq_student_id;
    
    ALTER TABLE persons 
    DROP CONSTRAINT uniq_company_and_uid_in_company;
    
    ALTER TABLE period_final_reports 
    DROP CONSTRAINT uniq_person;
    
    ALTER TABLE signature_texts 
    DROP CONSTRAINT uniq_sig_txt_document_and_person;
    
    ALTER TABLE signatures 
    DROP CONSTRAINT uniq_sig_document_and_person;
    
    ALTER TABLE survey 
    DROP CONSTRAINT uniq_internship_period;

""")
