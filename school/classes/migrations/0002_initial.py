# Generated by Django 4.2.4 on 2023-09-05 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("course", "0001_initial"),
        ("cycle", "0001_initial"),
        ("classes", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="class",
            name="course",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course.course"
            ),
        ),
        migrations.AddField(
            model_name="class",
            name="coursespercycle",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="course.coursespercycle"
            ),
        ),
        migrations.AddField(
            model_name="class",
            name="cycle",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="cycle.cycle"
            ),
        ),
    ]
