# Generated by Django 4.2.4 on 2023-09-18 16:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("attendance", "0008_alter_attendance_timearrive"),
    ]

    operations = [
        migrations.AlterField(
            model_name="attendance",
            name="timearrive",
            field=models.TimeField(default=datetime.time(16, 14, 39, 633643)),
        ),
    ]
