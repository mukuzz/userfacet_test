# Generated by Django 4.0.6 on 2022-07-29 07:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('class_booker', '0004_rename_student_name_booking_student_full_name_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TecherSchedule',
        ),
        migrations.AddField(
            model_name='booking',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.DateTimeField(max_length=10),
        ),
        migrations.AlterField(
            model_name='booking',
            name='start_time',
            field=models.CharField(max_length=10),
        ),
    ]