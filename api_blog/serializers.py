from blog.models import Post, Category, Comment
from django.contrib.auth.models import User, Group
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'name', 'body', 'date_added']


class PostSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'category', 'header_image', 'author_id', 'comments')

    comments = serializers.SerializerMethodField('get_comments')

    def get_comments(self, post):

        try:
            comment_post = Comment.objects.filter(post__id=post.id)
            return CommentSerializer(comment_post, many=True).data
        except Comment.DoesNotExist:
            return None

    def create(self, validated_data):

        post = Post.objects.get(pk=validated_data["author_id"])
        validated_data["post"] = post
        Post.objects.create(**validated_data)




class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'posts')

    posts = serializers.SerializerMethodField('get_posts')

    def get_posts(self, user):
        try:
            post_user = Post.objects.filter(author_id__id=user.id)
            return PostSerializer(post_user, many=True).data
        except Post.DoesNotExist:
            return None

