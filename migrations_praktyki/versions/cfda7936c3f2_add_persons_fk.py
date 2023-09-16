"""

add foreign keys

Revision ID: cfda7936c3f2
Creation date: 2023-09-10 18:37:51.647342

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cfda7936c3f2'
down_revision = 'ffafefc9a15e'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.execute("""
        ALTER TABLE applications  
        ADD CONSTRAINT fk_app_person_id
        FOREIGN KEY (student_id) 
        REFERENCES persons(person_id);
        
        ALTER TABLE applications  
        ADD CONSTRAINT fk_cv_id
        FOREIGN KEY (cv_id) 
        REFERENCES curriculum_vitae(id);
        
        ALTER TABLE audit_log  
        ADD CONSTRAINT fk_author_person
        FOREIGN KEY (author_of_log) 
        REFERENCES persons(person_id);
        
        ALTER TABLE audit_log  
        ADD CONSTRAINT fk_target_person
        FOREIGN KEY (target_of_log) 
        REFERENCES persons(person_id);
        
        ALTER TABLE curriculum_vitae  
        ADD CONSTRAINT fk_cv_person
        FOREIGN KEY (student_id) 
        REFERENCES persons(person_id);    
        
        ALTER TABLE days  
        ADD CONSTRAINT fk_internship_periods
        FOREIGN KEY (period_id) 
        REFERENCES internship_periods(id);
        
        ALTER TABLE ecdsa_keys
        ADD CONSTRAINT fk_owner_person
        FOREIGN KEY (owner_person_id)
        REFERENCES persons(person_id);
        
        ALTER TABLE internships
        ADD CONSTRAINT fk_internship_studentid
        FOREIGN KEY (student_id)
        REFERENCES persons(person_id);   
        
        ALTER TABLE internship_agreements
        ADD CONSTRAINT fk_ia_personid
        FOREIGN KEY (student_id)
        REFERENCES persons(person_id);   
        
        ALTER TABLE internship_agreements
        ADD CONSTRAINT fk_ia_app_id
        FOREIGN KEY (application_id)
        REFERENCES applications(id);     
        
        -- dodanie kolumny 
        ALTER TABLE internship_periods 
        ADD COLUMN agreement_id UUID;
        
        ALTER TABLE internship_periods
        ADD CONSTRAINT fk_ip_agg_id
        FOREIGN KEY (agreement_id)
        REFERENCES internship_agreements(id);     
        
        ALTER TABLE internship_periods
        ADD CONSTRAINT fk_ip_student_id
        FOREIGN KEY (student_id)
        REFERENCES persons(person_id);    
        
        ALTER TABLE period_final_reports
        ADD CONSTRAINT fk_pfr_student_id
        FOREIGN KEY (student_id)
        REFERENCES persons(person_id);
        
        ALTER TABLE period_final_reports
        ADD CONSTRAINT fk_pfr_period_id
        FOREIGN KEY (period_id)
        REFERENCES internship_periods(id);           
        
        ALTER TABLE persons
        ADD CONSTRAINT fk_company_id
        FOREIGN KEY (company_id)
        REFERENCES companies(id) ON DELETE SET NULL;  
        
        ALTER TABLE signatures
        ADD CONSTRAINT fk_sig_person_id
        FOREIGN KEY (person_id)
        REFERENCES persons(person_id);  
        
        ALTER TABLE signatures
        ADD CONSTRAINT fk_sig_key_id
        FOREIGN KEY (keyid)
        REFERENCES ecdsa_keys(key_id);
        
        ALTER TABLE signature_texts
        ADD CONSTRAINT fk_sig_texts_person_id
        FOREIGN KEY (person_id)
        REFERENCES persons(person_id);
        
        ALTER TABLE survey
        ADD CONSTRAINT fk_survey_ip_id
        FOREIGN KEY (internship_period_id)
        REFERENCES internship_periods(id);

    """)


def downgrade() -> None:
    op.execute("""
        ALTER TABLE applications
        DROP CONSTRAINT IF EXISTS fk_app_person_id;
        
        ALTER TABLE applications
        DROP CONSTRAINT IF EXISTS fk_cv_id;
        
        ALTER TABLE audit_log
        DROP CONSTRAINT IF EXISTS fk_author_person;
        
        ALTER TABLE audit_log
        DROP CONSTRAINT IF EXISTS fk_target_person;
        
        ALTER TABLE curriculum_vitae
        DROP CONSTRAINT IF EXISTS fk_cv_person;
        
        ALTER TABLE days
        DROP CONSTRAINT IF EXISTS fk_internship_periods;
        
        ALTER TABLE ecdsa_keys
        DROP CONSTRAINT IF EXISTS fk_owner_person;
        
        ALTER TABLE internships
        DROP CONSTRAINT IF EXISTS fk_internship_studentid;
        
        ALTER TABLE internship_agreements
        DROP CONSTRAINT IF EXISTS fk_ia_personid;
        
        ALTER TABLE internship_agreements
        DROP CONSTRAINT IF EXISTS fk_ia_app_id;
        
        ALTER TABLE internship_periods
        DROP CONSTRAINT IF EXISTS fk_ip_agg_id;
        
        ALTER TABLE internship_periods
        DROP CONSTRAINT IF EXISTS fk_ip_student_id;
        
        ALTER TABLE period_final_reports
        DROP CONSTRAINT IF EXISTS fk_pfr_student_id;
        
        ALTER TABLE period_final_reports
        DROP CONSTRAINT IF EXISTS fk_pfr_period_id;
        
        ALTER TABLE persons
        DROP CONSTRAINT IF EXISTS fk_company_id;
        
        ALTER TABLE signatures
        DROP CONSTRAINT IF EXISTS fk_sig_person_id;
        
        ALTER TABLE signatures
        DROP CONSTRAINT IF EXISTS fk_sig_key_id;
        
        ALTER TABLE signature_texts
        DROP CONSTRAINT IF EXISTS fk_sig_texts_person_id;
        
        ALTER TABLE survey
        DROP CONSTRAINT IF EXISTS fk_survey_ip_id;
   
    """)