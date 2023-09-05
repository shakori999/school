# Generated by Django 4.2.4 on 2023-09-05 09:37

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=100)),
                ("categorydescription", models.TextField()),
            ],
            options={
                "verbose_name_plural": "Categories",
            },
        ),
    ]
