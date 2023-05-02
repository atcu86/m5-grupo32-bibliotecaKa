from rest_framework_simplejwt.authentication import JWTAuthentication
from .models import User
from .serializers import UserSerializer, UserDetailSerializer
from .permissions import IsEmployee
from rest_framework import generics


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsEmployee]
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        return User.objects.filter(id=self.kwargs.get("user_id"))
