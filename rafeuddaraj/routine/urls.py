# urls.py
from .views import GetRoutineView
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GetRoutineView,RoutineView

router = DefaultRouter()
router.register(r'exam-schedule', RoutineView, basename='exam-schedule')


urlpatterns = [
    path('routine-show/', GetRoutineView.as_view(),
         name='exam-schedule-list-create'),
    path('exam-schedule/<int:pk>/', include(router.urls),
         name='exam-schedule-detail'),
    # Add more URLs as needed
]
