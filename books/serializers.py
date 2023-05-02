from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "synopsis",
            "published_date",
            "user_following",
        ]

    def create(self, validated_data):
        return Book.objects.create(**validated_data)
