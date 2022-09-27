from rest_framework.permissions import BasePermission,SAFE_METHODS

class MyIsAuthenticatedOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

class MyIsAdminUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff
