from rest_framework import permissions
from rest_framework.views import View, Request


class IsAuthorized(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        if request.method == "POST":
            return True
        if request.user.is_authenticated:
            if request.method == "PATCH":
                return obj.id == request.user.id
            if request.user.is_employee:
                return True
            else:
                return obj.id == request.user.id
        return False
