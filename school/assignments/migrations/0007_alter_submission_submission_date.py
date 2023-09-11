# Generated by Django 4.2.4 on 2023-09-11 09:17

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0006_alter_assignment_due_date"),
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
                            2023, 9, 11, 9, 17, tzinfo=datetime.timezone.utc
                        )
                    )
                ],
            ),
        ),
    ]