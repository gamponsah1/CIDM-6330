# Generated by Django 4.2.7 on 2024-04-22 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_course_first_upload_date_course_last_updated_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='first_upload_date',
        ),
        migrations.RemoveField(
            model_name='course',
            name='last_updated_date',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='instructor',
            name='date_of_death',
        ),
        migrations.AlterField(
            model_name='course',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
