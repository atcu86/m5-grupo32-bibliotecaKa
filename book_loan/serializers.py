from rest_framework import serializers
from .models import BookLoan


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

        if not user.is_allowed_lending:
            raise PermissionError("User cannot borrow the book")

        return BookLoan.objects.create(**validated_data, user=user)

    def update(self, instance, validated_data):
        print(validated_data)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        return instance
