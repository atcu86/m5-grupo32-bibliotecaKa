from rest_framework import serializers
from .models import BookLoan
from book_copy.models import BookCopy
from datetime import date, timedelta


class BookLoanSerializer(serializers.ModelSerializer):
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

    def create(self, validated_data):
        user = validated_data.pop("user")

        if user.date_block:
            first_date = user.date_block
            second_date = date.today()
            if first_date < second_date:
                user.is_allowed_lending = True
                user.date_block = None
                user.save()

        if not user.is_allowed_lending:
            raise serializers.ValidationError(
                {"message": "User doesn't have permission"}
            )

        return BookLoan.objects.create(**validated_data, user=user)

    def update(self, instance, validated_data):
        max_date = validated_data["book_loan"].max_return_date.strftime("%Y-%m-%d")
        devolution_date = date.today().strftime("%Y-%m-%d")

        if max_date < devolution_date:
            validated_data["user"].date_block = date.today() + timedelta(7)
            validated_data["user"].is_allowed_lending = False
            validated_data["user"].save()

        instance.returned_date = devolution_date
        instance.book_copy.is_available = True
        instance.book_copy.save()
        instance.save()

        return instance
