# Generated by Django 4.2.4 on 2023-08-27 09:32

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="teacher",
            options={"verbose_name_plural": "Teachers"},
        ),
        migrations.AlterModelOptions(
            name="teacherspercourse",
            options={"verbose_name_plural": "Teachers per Course"},
        ),
    ]
