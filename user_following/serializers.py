from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from .models import UserFollowing


class UserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ["id", "user", "book"]
        read_only_fields = ["book", "user"]

    def create(self, validated_data: dict):
        UserFollowing.objects.create(**validated_data)
        return Response(status=status.HTTP_200_OK)


