from rest_framework import serializers

from apps.posts.models import Post, Like, DisLike


class PostSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Post
        fields = ['id', 'title', 'like_rating', 'dislike_rating', 'user']


class LikeSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.title')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = Like
        fields = ['id', 'post', 'user', 'time']


class DisLikeSerializer(serializers.ModelSerializer):
    post = serializers.ReadOnlyField(source='post.title')
    user = serializers.ReadOnlyField(source='user.username')

    class Meta:
        model = DisLike
        fields = ['id', 'post', 'user', 'time']
