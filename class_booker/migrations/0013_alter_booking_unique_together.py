# Generated by Django 4.0.6 on 2022-07-29 08:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('class_booker', '0012_booking_day'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='booking',
            unique_together=set(),
        ),
    ]
