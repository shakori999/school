# Generated by Django 4.2.4 on 2023-08-24 13:53

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Assignment",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("title", models.CharField(max_length=200)),
                ("description", models.TextField()),
                (
                    "due_date",
                    models.DateField(
                        validators=[
                            django.core.validators.MinValueValidator(
                                limit_value=datetime.date(2023, 8, 24)
                            )
                        ]
                    ),
                ),
                ("description2", models.TextField()),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Submission",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("is_deleted", models.BooleanField(default=False)),
                ("submission_date", models.DateTimeField(auto_now_add=True)),
                ("file_upload", models.FileField(upload_to="submissions/")),
                (
                    "assignment",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="assignments.assignment",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
