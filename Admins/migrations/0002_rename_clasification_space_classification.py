from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('Admins', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='space',
            old_name='clasification',
            new_name='classification',
        ),
    ]
