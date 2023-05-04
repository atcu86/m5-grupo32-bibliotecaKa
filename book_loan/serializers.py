from rest_framework import serializers
from .models import BookLoan
from book_copy.models import BookCopy
from datetime import date, timedelta


class BookLoanSerializer(serializers.ModelSerializer):
    # max_return_date = serializers.SerializerMethodField()

    class Meta:
        model = BookLoan
        fields = [
            "id",
            "book_copy",
            "user",
            "loan_date",
            "max_return_date",
            "returned_date",
        ]

        extra_kwargs = {"book_copy": {"read_only": True}, "user": {"read_only": True}}

    def get_max_return_date(self, obj: BookCopy):
        # import ipdb
        # ipdb.set_trace()
        # devolution_book = date.today() + timedelta(
        #     int(obj.book_copy.is_avaliable)
        # )

        # if devolution_book.weekday() == 5:
        #     devolution_book = date.today() + timedelta(
        #         int(obj.book_copy.lending_time_limit) + 2
        #     )
        # if devolution_book.weekday() == 6:
        #     devolution_book = date.today() + timedelta(
        #         int(obj.book_copy.lending_time_limit) + 1
        #     )

        return date.today()

    def create(self, validated_data):
        user = validated_data.pop("user")

        if not user.is_allowed_lending:
            raise PermissionError("User cannot borrow the book")

        return BookLoan.objects.create(**validated_data, user=user)

    def update(self, instance, validated_data):
        print(validated_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
