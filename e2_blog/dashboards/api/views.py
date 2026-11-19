from rest_framework import generics
from dashboards.models import BlogPost
from .serializers import BlogPostSerializer
from drf_spectacular.utils import extend_schema

@extend_schema(summary="List all dashboard blog posts", tags=["Dashboard"])
class BlogPostListAPIView(generics.ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
