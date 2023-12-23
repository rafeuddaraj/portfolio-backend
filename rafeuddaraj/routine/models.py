from django.db import models
from django.utils import timezone


class ExamSchedule(models.Model):
    STATUS_CHOICES = (
        (1, 'Pending'),
        (2, 'InProgress'),
        (3, 'Complete'),
    )

    date = models.DateTimeField()
    start_time = models.TimeField()
    end_time = models.TimeField()
    subject = models.CharField(max_length=255)
    subject_code = models.CharField(max_length=20)
    room_number = models.CharField(max_length=10)
    status = models.IntegerField(choices=STATUS_CHOICES, default=1)

    def __str__(self):
        return f"{self.date} - {self.subject}"

    def save(self, *args, **kwargs):
        current_datetime = timezone.now()
        exam_datetime_start = timezone.make_aware(timezone.datetime.combine(self.date, self.start_time))
        exam_datetime_end = timezone.make_aware(timezone.datetime.combine(self.date, self.end_time))

        if current_datetime >= exam_datetime_start and current_datetime < exam_datetime_end:
            self.status = 2  # InProgress
        elif current_datetime >= exam_datetime_end:
            self.status = 3  # Complete
        else:
            self.status = 1  # Pending

        super().save(*args, **kwargs)
