from rest_framework import permissions
from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        elif request.method == "GET":
            return True
        return False
