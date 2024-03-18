#0018_add_trigger.py
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_remove_farm_budget'),  
    ]

    operations = [
        migrations.RunSQL(
            """
            CREATE OR REPLACE FUNCTION check_total_amount()
            RETURNS TRIGGER AS $$
            BEGIN
                IF NEW.total_amount < 0 THEN
                    RAISE EXCEPTION 'Total amount of sale cannot be negative. Please insert a positive value.';
                END IF;
                RETURN NEW;
            END;
            $$ LANGUAGE plpgsql;

            CREATE TRIGGER trigger_check_total_amount
            BEFORE INSERT OR UPDATE ON app_sale
            FOR EACH ROW
            EXECUTE FUNCTION check_total_amount();
            """
        ),
    ]
