# Generated by Django 3.0.6 on 2023-09-26 17:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0011_auto_20230926_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='timearrive',
            field=models.TimeField(default=datetime.time(17, 22, 21, 586366)),
        ),
    ]