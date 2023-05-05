from rest_framework import permissions
from rest_framework.views import View


class IsEmployeeOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view: View) -> bool:
        if request.method == "GET":
            return True
        if request.method == "POST":
            return request.user.is_authenticated and request.user.is_employee
<<<<<<< HEAD
  
=======


>>>>>>> 9e33826ebd59ccd01fbd6c9947b106f7942c37fa
class IsEmployee(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        return request.user.is_authenticated and request.user.is_employee
