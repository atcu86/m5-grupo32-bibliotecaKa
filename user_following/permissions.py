from rest_framework import permissions
from rest_framework.views import View, Request
from .models import User


class IsStudent(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.user.is_authenticated:
            if request.user.is_employee:
                return False
            else:
                return True
        return False


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated and request.user.is_employee
