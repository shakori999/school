# Generated by Django 3.0.6 on 2023-09-27 07:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0016_auto_20230927_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='timearrive',
            field=models.TimeField(default=datetime.datetime(2023, 9, 27, 7, 35, 39, 968056, tzinfo=utc)),
        ),
    ]
