# Generated by Django 4.2.4 on 2023-08-27 03:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("dashboard", "0001_initial"),
        ("course", "0001_initial"),
        ("cycle", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                ("teachername", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phoneno", models.CharField(max_length=20)),
                ("subject_taught", models.CharField(max_length=50)),
                ("date_of_birth", models.DateField()),
                ("address", models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name="TeachersPerCourse",
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
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
                (
                    "coursespercycle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="course.coursespercycle",
                    ),
                ),
                (
                    "cycle",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cycle.cycle"
                    ),
                ),
                (
                    "teacher",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="teacher.teacher",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="teacher",
            name="courses",
            field=models.ManyToManyField(
                through="teacher.TeachersPerCourse", to="course.course"
            ),
        ),
        migrations.AddField(
            model_name="teacher",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE, to="dashboard.person"
            ),
        ),
    ]
