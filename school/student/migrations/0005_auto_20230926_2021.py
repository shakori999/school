# Generated by Django 3.0.6 on 2023-09-26 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0004_alter_student_email_alter_student_phoneno'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='student',
            options={'ordering': ['phoneno'], 'verbose_name_plural': 'Students'},
        ),
        migrations.AlterField(
            model_name='enrollment',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
