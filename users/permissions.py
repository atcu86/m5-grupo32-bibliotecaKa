from rest_framework import permissions
from rest_framework.views import View, Request


class IsEmployee(permissions.BasePermission):
    def has_permission(self, request: Request, view: View) -> bool:
        if request.method == "POST":
            return True
        else:
            return request.user.is_authenticated and request.user.is_superuser


class IsEmployeeOrOwner(permissions.BasePermission):
    def has_object_permission(self, request: Request, view: View, obj) -> bool:
        if request.user.is_authenticated:
            if request.user.is_employee:
                return True
            else:
                return obj.id == request.user.id
        return False
