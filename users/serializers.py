from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "email", "first_name", "last_name", "is_allowed_lending", "date_block"]


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "first_name",
            "last_name",
            "is_employee",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with that username already exists.",
                    )
                ]
            },
            "email": {
                "validators": [
                    UniqueValidator(
                        queryset=User.objects.all(),
                        message="A user with this email already exists.",
                    )
                ]
            },
        }

    def create(self, validated_data: dict):
        if validated_data.get("is_employee", False):
            if validated_data["is_employee"]:
                return User.objects.create_superuser(**validated_data)
        return User.objects.create_user(**validated_data)
