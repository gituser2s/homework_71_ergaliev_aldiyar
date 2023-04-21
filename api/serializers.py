from rest_framework import serializers
from posts.models.posts import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'likes_count', 'description', 'image', 'author', 'is_deleted')
        read_only_fields = ('is_deleted',)
