from django.urls import path
from .views import BlogPostListAPIView

urlpatterns = [
    path('dashboard-blogs/', BlogPostListAPIView.as_view(), name='dashboard_blogs_api'),
]
