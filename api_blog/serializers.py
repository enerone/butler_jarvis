from blog.models import Post, Category, Comment
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'category', 'header_image', 'author_id')

