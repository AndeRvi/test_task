from rest_framework import serializers

from posts.models import Post, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
             'text', 'id',
        ]
        read_only_fields = ['id']


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = [
            'id', 'response'
        ]
        read_only_fields = ['id']
