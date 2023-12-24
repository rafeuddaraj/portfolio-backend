from django.db import models
from django.utils import timezone


class ExamSchedule(models.Model):
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'InProgress'),
        (3, 'Complete'),
    )

    date = models.DateTimeField()
    start_time = models.DateTimeField(null=True)
    end_time = models.DateTimeField(null=True)
    subject = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=20)
    room_number = models.CharField(max_length=10)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.date} - {self.subject}"
