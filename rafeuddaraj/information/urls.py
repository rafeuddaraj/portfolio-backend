from django.urls import path
from .views import UserInformation

urlpatterns = [
    path('',UserInformation.as_view())
]
