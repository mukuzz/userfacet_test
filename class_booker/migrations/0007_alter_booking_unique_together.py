# Generated by Django 4.0.6 on 2022-07-29 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_booker', '0006_alter_booking_end_time'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together={('date', 'start_time', 'end_time', 'teacher_full_name')},
        ),
    ]
