from django.shortcuts import render
from rest_framework import viewsets
from api_blog.serializers import PostSerializer
from blog.models import Post
from rest_framework.permissions import IsAuthenticated


# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = Post.objects.all().order_by('title')
    serializer_class = PostSerializer
