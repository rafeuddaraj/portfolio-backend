# views.py
from rest_framework import generics, permissions
from rest_framework.viewsets import ModelViewSet
from .models import ExamSchedule
from .serializers import ExamScheduleSerializer


class GetRoutineView(generics.ListAPIView):
    queryset = ExamSchedule.objects.all()
    serializer_class = ExamScheduleSerializer

    class Meta:
        fields = '__all__'

class RoutineView(ModelViewSet):
    queryset = ExamSchedule.objects.all()
    serializer_class = ExamScheduleSerializer
    permission_classes = [permissions.IsAdminUser]