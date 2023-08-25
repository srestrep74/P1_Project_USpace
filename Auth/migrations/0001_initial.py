# Generated by Django 4.2.4 on 2023-08-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.IntegerField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150, unique=True)),
                ('account_type', models.IntegerField(editable=False)),
            ],
        ),
    ]
