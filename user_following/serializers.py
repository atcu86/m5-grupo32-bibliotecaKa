from rest_framework import serializers

from .models import UserFollowing


class UserFollowingSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserFollowing
        fields = ["id", "user", "book"]
        read_only_fields = ["book", "user"]

    def create(self, validated_data: dict):
        return UserFollowing.objects.create(**validated_data)
