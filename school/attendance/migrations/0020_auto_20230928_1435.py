# Generated by Django 3.0.6 on 2023-09-28 11:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0019_auto_20230928_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='timearrive',
            field=models.TimeField(default=datetime.datetime(2023, 9, 28, 11, 35, 38, 122376, tzinfo=utc)),
        ),
    ]