# Generated by Django 3.0.6 on 2023-09-26 17:21

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0010_alter_attendance_timearrive'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='timearrive',
            field=models.TimeField(default=datetime.time(17, 21, 42, 102097)),
        ),
    ]