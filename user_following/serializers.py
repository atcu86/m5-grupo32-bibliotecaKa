from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import UserFollowing


class UserFollowingSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    book = serializers.SerializerMethodField()

    class Meta:
        model = UserFollowing
        fields = ["id", "user", "book"]
        read_only_fields = ["book", "user"]

    def create(self, validated_data: dict):
        return UserFollowing.objects.create(**validated_data)

    def get_user(self, obj):
        dict = {"id": obj.user.id, "username": obj.user.username}
        return dict

    def get_book(self, obj):
        dict = {"id": obj.book.id, "title": obj.book.title}
        return dict
