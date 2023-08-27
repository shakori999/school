# Generated by Django 4.2.4 on 2023-08-27 09:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("exames", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="test",
            options={"verbose_name_plural": "Tests"},
        ),
        migrations.AlterModelOptions(
            name="testsscores",
            options={"verbose_name_plural": "Tests Scores"},
        ),
        migrations.AlterField(
            model_name="test",
            name="testno",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
        migrations.AlterField(
            model_name="testsscores",
            name="score",
            field=models.DecimalField(
                decimal_places=2,
                max_digits=5,
                validators=[
                    django.core.validators.MinValueValidator(0),
                    django.core.validators.MaxValueValidator(100),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="testsscores",
            name="testsno",
            field=models.IntegerField(
                validators=[django.core.validators.MinValueValidator(1)]
            ),
        ),
    ]
