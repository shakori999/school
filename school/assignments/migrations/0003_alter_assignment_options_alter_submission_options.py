# Generated by Django 4.2.4 on 2023-08-27 09:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("assignments", "0002_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="assignment",
            options={"verbose_name_plural": "Assignments"},
        ),
        migrations.AlterModelOptions(
            name="submission",
            options={"verbose_name_plural": "Submissions"},
        ),
    ]
