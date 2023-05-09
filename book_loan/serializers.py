from rest_framework import serializers
from .models import BookLoan
from book_copy.models import BookCopy
from user_following.models import UserFollowing
from users.models import User
from books.models import Book
from datetime import date, timedelta
from django.core.mail import send_mail
from django.conf import settings


class BookLoanSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()
    book_copy = serializers.SerializerMethodField()
    user_id = serializers.UUIDField()

    def get_user(self, obj):
        dict = {
            "id": obj.user.id,
            "username": obj.user.username,
        }
        return dict

    def get_book_copy(self, obj):
        dict = {"id": obj.book_copy.id, "title_book": obj.book_copy.book.title}
        return dict

    class Meta:
        model = BookLoan
        fields = [
            "id",
            "book_copy",
            "user",
            "loan_date",
            "max_return_date",
            "returned_date",
            "user_id",
        ]

        extra_kwargs = {"book_copy": {"read_only": True}, "user": {"read_only": True}}
        depth = 1

    def create(self, validated_data):
        user = validated_data.pop("user")
        second_date = date.today()

        book_loan = BookLoan.objects.filter(user=user)

        for books in book_loan:
            if not books.returned_date:
                if books.max_return_date.strftime("%Y-%m-%d") < second_date.strftime(
                    "%Y-%m-%d"
                ):
                    raise serializers.ValidationError(
                        {
                            "message": f"There are still pendencies for this user - {books.book_copy.book.title}"
                        }
                    )

        if user.date_block:
            first_date = user.date_block
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

        count = 0
        all_copy = BookCopy.objects.all()
        specific_copy = BookCopy.objects.filter(id=self.data["book_copy"]["id"]).first()
        all_followers = UserFollowing.objects.filter(book_id=specific_copy.book_id)
        found_book = Book.objects.filter(id=specific_copy.book_id).first()
        for copy in all_copy:
            if copy.is_available:
                count += 1

        if count == 1:
            for follower in all_followers:
                found_user = User.objects.filter(id=follower.user_id).first()
                username = found_user.username
                email = found_user.email
                send_mail(
                    subject="Seu livro está disponível!",
                    message=f"Atenção {username}, o livro {found_book.title} está disponível.",
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[f"{email}"],
                    fail_silently=False,
                )

        return instance
