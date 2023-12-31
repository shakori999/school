# Generated by Django 4.2.4 on 2023-09-12 06:44

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0008_alter_assignment_due_date_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="submission",
            name="submission_date",
            field=models.DateTimeField(
                auto_now_add=True,
                validators=[
                    django.core.validators.MinValueValidator(
                        limit_value=datetime.datetime(
                            2023, 9, 12, 6, 44, tzinfo=datetime.timezone.utc
                        )
                    )
                ],
            ),
        ),
    ]
