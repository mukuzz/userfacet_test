import email
from django.db import models
from django.utils import timezone


class Booking(models.Model):
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(default=timezone.now)
    teacher_full_name = models.CharField(max_length=256)
    teacher_email = models.EmailField(max_length=256)
    student_full_name = models.CharField(max_length=256)
    student_email = models.EmailField(max_length=256)

    class Meta:
        unique_together = (("start_time", "end_time", "teacher_full_name"),)