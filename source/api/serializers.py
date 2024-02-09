from rest_framework import serializers
from webapp.models import Publication


class PublicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publication
        fields = ['id', 'picture', 'description', 'likes_count', 'comments_count', 'author', 'created', 'users_like']
        read_only_fields = ['likes_count', 'comments_count', 'created', 'users_like', 'author']
