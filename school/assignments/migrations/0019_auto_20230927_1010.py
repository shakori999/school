# Generated by Django 3.0.6 on 2023-09-27 07:10

import datetime
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0018_auto_20230926_2021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 9, 27))]),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_date',
            field=models.DateField(default=django.utils.timezone.now, validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 9, 27))]),
        ),
    ]
