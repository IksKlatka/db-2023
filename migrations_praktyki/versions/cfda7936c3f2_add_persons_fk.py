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
    
    ALTER TABLE internship_periods
        ADD CONSTRAINT internship_periods_student_id__persons_person_id
            FOREIGN KEY (student_id) REFERENCES persons(person_id);
    ALTER TABLE internships
        ADD CONSTRAINT internships_student_id__persons_person_id
            FOREIGN KEY (student_id) REFERENCES persons(person_id);
            
    ALTER TABLE period_final_reports
        ADD CONSTRAINT period_final_reports_student_id__persons_person_id
            FOREIGN KEY (student_id) REFERENCES persons(person_id);
    ALTER TABLE period_final_reports
        ADD CONSTRAINT period_final_reports_period_id__internship_periods_id
            FOREIGN KEY (period_id) REFERENCES internship_periods(id);

    ALTER TABLE applications
        ADD CONSTRAINT applications_student_id__persons__person_id
            FOREIGN KEY (student_id) REFERENCES persons(person_id);

    ALTER TABLE applications
        ADD CONSTRAINT applications_cvid__curriculum_vitae_id
            FOREIGN KEY (cv_id) REFERENCES curriculum_vitae(id);

    ALTER TABLE internship_agreements
        ADD CONSTRAINT internship_agreements_student_id__persons_person_id
            FOREIGN KEY (student_id) REFERENCES persons(person_id);

    ALTER TABLE ecdsa_keys
        ADD CONSTRAINT ecdsa_keys_owner_person_id__persons_person_id
            FOREIGN KEY (owner_person_id) REFERENCES persons(person_id);

    ALTER TABLE curriculum_vitae
        ADD CONSTRAINT curriculum_vitae_student_id__persons_person_id
            FOREIGN KEY (student_id) REFERENCES persons(person_id);

    ALTER TABLE days
        ADD CONSTRAINT days_period_id__internship_periods_id
            FOREIGN KEY (period_id) REFERENCES internship_periods(id);

    ALTER TABLE audit_log
        ADD CONSTRAINT audit_log_author_of_log__persons_person_id
            FOREIGN KEY (author_of_log) REFERENCES persons(person_id);
    ALTER TABLE audit_log
        ADD CONSTRAINT audit_log_target_of_log__persons_person_id
            FOREIGN KEY (target_of_log) REFERENCES persons(person_id);

    ALTER TABLE signature_texts
        ADD CONSTRAINT signature_texts_person_id__persons_person_id
            FOREIGN KEY (person_id) REFERENCES persons(person_id);

    ALTER TABLE signatures
        ADD CONSTRAINT signatures_person_id__persons_person_id
            FOREIGN KEY (person_id) REFERENCES persons(person_id);
        
    ALTER TABLE survey_answer
        ALTER COLUMN question TYPE UUID USING question::UUID;

    ALTER TABLE survey_answer
    ADD CONSTRAINT survey_answer_question__survey_question_id
        FOREIGN KEY (question) REFERENCES survey_question(id);
    """)


def downgrade() -> None:
    op.execute("""
    ALTER TABLE internship_periods
        DROP CONSTRAINT internship_periods_student_id__persons_person_id CASCADE;
    ALTER TABLE internships
        DROP CONSTRAINT internships_student_id__persons_person_id CASCADE;

    ALTER TABLE period_final_reports
        DROP CONSTRAINT period_final_reports_student_id__persons_person_id CASCADE;
    ALTER TABLE period_final_reports
        DROP CONSTRAINT period_final_reports_period_id__internship_periods_id CASCADE;

    ALTER TABLE applications
        DROP CONSTRAINT applications_student_id__persons__person_id CASCADE;

    ALTER TABLE applications
        DROP CONSTRAINT applications_cvid__curriculum_vitae_id CASCADE;

    ALTER TABLE internship_agreements
        DROP CONSTRAINT internship_agreements_student_id__persons_person_id CASCADE;

    ALTER TABLE ecdsa_keys
        DROP CONSTRAINT ecdsa_keys_owner_person_id__persons_person_id CASCADE;

    ALTER TABLE curriculum_vitae
        DROP CONSTRAINT curriculum_vitae_student_id__persons_person_id CASCADE;

    ALTER TABLE days
        DROP CONSTRAINT days_period_id__internship_periods_id CASCADE;

    ALTER TABLE audit_log
        DROP CONSTRAINT audit_log_author_of_log__persons_person_id CASCADE;
    ALTER TABLE audit_log
        DROP CONSTRAINT audit_log_target_of_log__persons_person_id CASCADE;

    ALTER TABLE signature_texts
        DROP CONSTRAINT signature_texts_person_id__persons_person_id CASCADE;

    ALTER TABLE signatures
        DROP CONSTRAINT signatures_person_id__persons_person_id CASCADE;
   
    ALTER TABLE survey_answer
        DROP CONSTRAINT survey_answer_question__survey_question_id CASCADE;

    ALTER TABLE survey_answer
        ALTER COLUMN question TYPE TEXT USING question::TEXT;
    
    """)