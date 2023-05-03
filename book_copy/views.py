from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .serializers import BookCopySerializer


# Create your views here.

class BookCopyCreateView(generics.CreateAPIView):
    serializer_class = BookCopySerializer
    permission_classes = [IsAuthenticated]