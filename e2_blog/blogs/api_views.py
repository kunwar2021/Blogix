from rest_framework import viewsets, generics
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from rest_framework.pagination import PageNumberPagination
from django.contrib.auth.models import User
from drf_spectacular.utils import extend_schema, extend_schema_view

from .models import Category, Blogs, Comment
from .serializers import CategorySerializer, BlogSerializer, CommentSerializer, UserSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 100


@extend_schema_view(
    list=extend_schema(summary="List all blog categories", tags=["Categories"]),
    retrieve=extend_schema(summary="Retrieve category details", tags=["Categories"]),
    create=extend_schema(summary="Create a new blog category", tags=["Categories"]),
    update=extend_schema(summary="Update a category", tags=["Categories"]),
    partial_update=extend_schema(summary="Partially update a category", tags=["Categories"]),
    destroy=extend_schema(summary="Delete a category", tags=["Categories"]),
)
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all().order_by('-created_at')
    serializer_class = CategorySerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]


@extend_schema_view(
    list=extend_schema(summary="List all blog posts with pagination", tags=["Blogs"]),
    retrieve=extend_schema(summary="Retrieve blog post details", tags=["Blogs"]),
    create=extend_schema(summary="Create a new blog post", tags=["Blogs"]),
    update=extend_schema(summary="Update a blog post", tags=["Blogs"]),
    partial_update=extend_schema(summary="Partially update a blog post", tags=["Blogs"]),
    destroy=extend_schema(summary="Delete a blog post", tags=["Blogs"]),
)
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blogs.objects.all().order_by('-created_at')
    serializer_class = BlogSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]


@extend_schema_view(
    list=extend_schema(summary="List all comments", tags=["Comments"]),
    retrieve=extend_schema(summary="Retrieve comment details", tags=["Comments"]),
    create=extend_schema(summary="Create a comment on a blog post", tags=["Comments"]),
    update=extend_schema(summary="Update a comment", tags=["Comments"]),
    partial_update=extend_schema(summary="Partially update a comment", tags=["Comments"]),
    destroy=extend_schema(summary="Delete a comment", tags=["Comments"]),
)
class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]


@extend_schema_view(
    list=extend_schema(summary="List all registered users", tags=["Users"]),
    retrieve=extend_schema(summary="Retrieve user profile details", tags=["Users"]),
    create=extend_schema(summary="Create a user account", tags=["Users"]),
    update=extend_schema(summary="Update a user account", tags=["Users"]),
    partial_update=extend_schema(summary="Partially update a user account", tags=["Users"]),
    destroy=extend_schema(summary="Delete a user account", tags=["Users"]),
)
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('id')
    serializer_class = UserSerializer
    pagination_class = StandardResultsSetPagination
    permission_classes = [IsAuthenticatedOrReadOnly]


@extend_schema(summary="Public user registration endpoint", tags=["Authentication"])
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]