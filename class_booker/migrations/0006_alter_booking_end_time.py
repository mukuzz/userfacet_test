# Generated by Django 4.0.6 on 2022-07-29 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class_booker', '0005_delete_techerschedule_booking_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='end_time',
            field=models.CharField(max_length=10),
        ),
    ]
