# Generated by Django 4.2.4 on 2023-09-05 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("attendance", "0001_initial"),
        ("classes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="attendance",
            name="class_info",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="classes.class"
            ),
        ),
    ]
