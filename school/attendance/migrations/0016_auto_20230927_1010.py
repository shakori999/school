# Generated by Django 3.0.6 on 2023-09-27 07:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0015_auto_20230926_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='timearrive',
            field=models.TimeField(default=datetime.time(7, 10, 29, 783253)),
        ),
    ]
