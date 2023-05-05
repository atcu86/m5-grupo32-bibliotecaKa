from rest_framework import permissions
from rest_framework.views import View


class IsEmployeeOrOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.user.is_employee:
                return True
            else:
                user_id = request.user.id
                url_id = view.kwargs.get("user_id")
                return str(user_id) == str(url_id)
        return False
