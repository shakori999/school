# Generated by Django 3.0.6 on 2023-09-28 08:15

import datetime
import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('assignments', '0019_auto_20230927_1010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='assignment',
            name='due_date',
            field=models.DateField(validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 9, 28))]),
        ),
        migrations.AlterField(
            model_name='submission',
            name='submission_date',
            field=models.DateField(default=django.utils.timezone.now, validators=[django.core.validators.MinValueValidator(limit_value=datetime.date(2023, 9, 28))]),
        ),
    ]
