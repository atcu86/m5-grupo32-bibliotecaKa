from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import UserFollowing
from .serializers import UserFollowingSerializer
from .permissions import IsStudent, IsAuthenticatedOrOwner
from rest_framework import generics
from books.models import Book
from django.shortcuts import get_object_or_404
from rest_framework import serializers
from rest_framework import status
from rest_framework.response import Response
from users.serializers import UserSerializer
from users.models import User


class UserFollowingView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsStudent]
    queryset = UserFollowing.objects.all()
    serializer_class = UserFollowingSerializer
    lookup_url_kwarg = "book_id"

    def perform_create(self, serializer):
        book = get_object_or_404(Book, id=self.kwargs.get("book_id"))
        if UserFollowing.objects.filter(book=book, user=self.request.user).exists():
            raise serializers.ValidationError("You are already following this book.")
        else:
            serializer.save(book=book, user=self.request.user)
            return Response(status=status.HTTP_200_OK)


class BookFollowersView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrOwner]
    queryset = UserFollowing.objects.all()
    serializer_class = UserSerializer
    lookup_url_kwarg = "book_id"

    def get_queryset(self):
        all_following = UserFollowing.objects.filter(book_id=self.kwargs.get("book_id"))
        all_users = []
        for item in all_following:
            all_users.append(User.objects.get(id=item.user_id))
        return all_users
