# Generated by Django 5.1.2 on 2024-10-30 18:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 30, 18, 48, 47, 751911, tzinfo=datetime.timezone.utc)),
        ),
    ]
