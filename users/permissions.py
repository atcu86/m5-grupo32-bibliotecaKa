from rest_framework import permissions
from rest_framework.views import View, Request


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        return request.user.is_authenticated and request.user.is_superuser
