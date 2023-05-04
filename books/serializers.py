from rest_framework import serializers
from .models import Book
from genres.models import Genre
from genres.serializers import GenreSerializer
from book_copy.models import BookCopy


class BookSerializer(serializers.ModelSerializer):
    genres = GenreSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "synopsis",
            "published_date",
            "publishing_company",
            "language",
            "days_to_borrow",
            "genres",
            "quantity",
            "user_following",
        ]

    def create(self, validated_data: dict) -> Book:
        genre_data = validated_data.pop("genres")
        book = Book.objects.create(**validated_data)
        for value in genre_data:
            found_genre = Genre.objects.filter(name=value["name"]).first()
            if not found_genre:
                found_genre = Genre.objects.create(name=value["name"])
            book.genres.add(found_genre)

        book.save()

        for i in range(validated_data["quantity"]):
            BookCopy.objects.create(book=book)

        return book
