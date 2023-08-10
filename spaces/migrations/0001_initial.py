# Generated by Django 4.2.4 on 2023-08-10 20:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('outh', '0001_initial'),
        ('admins', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('rating', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5)])),
                ('comment', models.CharField(max_length=500)),
                ('space_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.spaces')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outh.users')),
            ],
        ),
        migrations.CreateModel(
            name='Reminders',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('remember_to', models.DateTimeField()),
                ('space_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='admins.spaces')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='outh.users')),
            ],
        ),
    ]
