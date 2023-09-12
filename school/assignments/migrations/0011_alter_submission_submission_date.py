# Generated by Django 4.2.4 on 2023-09-12 06:53

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0010_alter_submission_submission_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="submission_date",
            field=models.DateTimeField(
                default=datetime.date(2023, 9, 12),
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.date(2023, 9, 12)
                    )
                ],
            ),
        ),
    ]
