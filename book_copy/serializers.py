from rest_framework import serializers
from book_copy.models import BookCopy


class BookCopySerializer(serializers.ModelSerializer):

    class Meta:
        model = BookCopy
        fields = ('id', 'book__title', 'book__author', "lending_time_limit", "book_loans") # o underline duplo é para acessar os dados da model book