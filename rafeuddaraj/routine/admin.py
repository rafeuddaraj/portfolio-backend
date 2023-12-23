from django.contrib import admin
from .models import ExamSchedule

# Register your models here.
class ExamScheduleAdmin(admin.ModelAdmin):
    model = ExamSchedule

admin.site.register(ExamSchedule, ExamScheduleAdmin)
