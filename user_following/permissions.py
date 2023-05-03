from rest_framework import permissions
from rest_framework.views import View, Request


class IsStudent(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.user.is_authenticated:
            if request.user.is_superuser:
                return False
            else:
                return True
        return False
