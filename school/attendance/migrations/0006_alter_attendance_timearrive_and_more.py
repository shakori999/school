# Generated by Django 4.2.4 on 2023-09-15 06:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0005_alter_attendance_timearrive"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="timearrive",
            field=models.TimeField(default=datetime.time(6, 25, 34, 591603)),
        ),
        migrations.AlterField(
            model_name="attendance",
            name="timeleave",
            field=models.TimeField(),
        ),
    ]
