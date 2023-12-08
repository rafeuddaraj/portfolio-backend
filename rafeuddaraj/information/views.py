from rest_framework.generics import ListAPIView
from .serializers import UserInfoSerializer
from .models import UserInfo
# Create your views here.
class UserInformation (ListAPIView):
    queryset = UserInfo.objects.all()
    serializer_class = UserInfoSerializer