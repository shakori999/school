# Generated by Django 4.2.4 on 2023-09-14 07:47

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("teacher", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="teacher",
            name="password",
            field=models.CharField(default="teacherpass123", max_length=100),
        ),
    ]
