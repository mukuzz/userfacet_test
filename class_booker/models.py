import email
from django.db import models
from django.utils import timezone


class Booking(models.Model):
    date = models.DateField(default=timezone.now)
    start_time = models.CharField(max_length=10)
    end_time = models.CharField(max_length=10)
    teacher_full_name = models.CharField(max_length=256)
    teacher_email = models.EmailField(max_length=256)
    student_full_name = models.CharField(max_length=256)
    student_email = models.EmailField(max_length=256)

    class Meta:
        unique_together = (("date", "start_time", "end_time", "teacher_full_name"),)