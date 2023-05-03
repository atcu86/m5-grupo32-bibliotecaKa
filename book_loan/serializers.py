from rest_framework import serializers
from .models import BookLoan
from book_copy import BookCopy
from datetime import date, timedelta


class BookLoanSerializer(serializers.ModelSerializer):
    max_return_date = serializers.SerializerMethodField()

    def get_max_return_date(self, obj: BookCopy):
        devolution_book = date.today() + timedelta(int(obj.book_copy.lending_time_limit))

        if devolution_book.weekday() == 5:
            devolution_book = date.today() + timedelta(int(obj.book_copy.lending_time_limit) + 2)
        if devolution_book.weekday() == 6:
            devolution_book = date.today() + timedelta(int(obj.book_copy.lending_time_limit) + 1)

        return devolution_book

    class Meta:
        model = BookLoan
        fields = [
            'id',
            'book',
            'user',
            'loan_date',
            'max_return_date',
            'returned_date',
        ]

    def create(self, validated_data):
        return BookLoan.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
