# Generated by Django 3.0.6 on 2023-09-28 11:36

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0020_auto_20230928_1435'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='timearrive',
            field=models.TimeField(default=django.utils.timezone.now),
        ),
    ]
