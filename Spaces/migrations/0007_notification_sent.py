# Generated by Django 4.2.4 on 2023-10-01 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Spaces', '0006_remove_notification_scheduled_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='sent',
            field=models.BooleanField(default=False),
        ),
    ]
