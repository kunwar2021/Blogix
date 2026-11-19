from rest_framework import serializers
from .models import Category, Blogs, Comment
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        user = User.objects.create_user(**validated_data)
        if password:
            user.set_password(password)
            user.save()
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'category_name', 'created_at', 'updated_at']


class BlogSerializer(serializers.ModelSerializer):
    category_detail = CategorySerializer(source='category', read_only=True)
    author_detail = UserSerializer(source='author', read_only=True)

    class Meta:
        model = Blogs
        fields = [
            'id', 'title', 'slug', 'category', 'category_detail',
            'author', 'author_detail', 'blog_image', 'short_description',
            'blog_body', 'status', 'is_feacherd', 'created_at', 'updated_at'
        ]
        read_only_fields = ['created_at', 'updated_at']


# Alias for backward compatibility
BlogsSerializer = BlogSerializer


class CommentSerializer(serializers.ModelSerializer):
    user_detail = UserSerializer(source='user', read_only=True)
    blog_detail = BlogSerializer(source='blog', read_only=True)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'user_detail', 'blog', 'blog_detail', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['created_at', 'updated_at']