from django.urls import path
from .views import (
    ServicesView,
    ClientView,
    BlogView,
    ResumeView,
    CommentView,
    PackageView,
    CategoryView,
    PortfolioView,
    ClientsReviewView,
    ClientsReviewDetailView,
    SkillsView,
    EducationView
)

urlpatterns = [
    path("services/", ServicesView.as_view(), name="services-list"),
    path("clients/", ClientView.as_view(), name="clients-list"),
    path("blogs/", BlogView.as_view(), name="blogs-list"),
    path("resume/", ResumeView.as_view(), name="resume-list"),
    path("comments/", CommentView.as_view(), name="comments-list"),
    path("packages/", PackageView.as_view(), name="packages-list"),
    path("categories/", CategoryView.as_view(), name="categories-list"),
    path("portfolio/", PortfolioView.as_view(), name="portfolio-list"),
    path("clients_review/", ClientsReviewView.as_view(), name="clients-review-list"),
    path("clients_review/<int:pk>/", ClientsReviewDetailView.as_view(), name="clients-review-detail-list"),
    path("skills/", SkillsView.as_view(), name="skills"),
    path("educations/", EducationView.as_view(), name="educations"),
]
