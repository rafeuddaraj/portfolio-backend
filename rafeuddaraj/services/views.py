from rest_framework.generics import ListAPIView
from .serializers import (
    ServicesSerializer,
    BlogSerializer,
    CategorySerializer,
    ClientSerializer,
    ClientsReviewSerializer,
    CommentSerializer,
    PackageSerializer,
    PortfolioSerializer,
    ResumeSerializer
)
from .models import (
    Services,
    Blog,
    Category,
    Client,
    ClientsReview,
    Comment,
    Package,
    Portfolio,
    Resume
)

# Create your views here.

class ServicesView(ListAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer

class BlogView(ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class CategoryView(ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class ClientView(ListAPIView):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer

class ClientsReviewView(ListAPIView):
    queryset = ClientsReview.objects.all()
    serializer_class = ClientsReviewSerializer

class CommentView(ListAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class PackageView(ListAPIView):
    queryset = Package.objects.all()
    serializer_class = PackageSerializer

class PortfolioView(ListAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer

class ResumeView(ListAPIView):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer
