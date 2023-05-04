from rest_framework import permissions
from rest_framework.views import View, Request
from .models import User


class IsStudent(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return False
            else:
                return True
        return False


class IsAuthenticatedOrOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj: User) -> bool:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return True
            else:
                return obj.id == request.user.id
        return False
