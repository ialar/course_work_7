from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    """Проверяет, является ли пользователь владельцем объекта."""

    def has_object_permission(self, request, view, obj):
        if obj.owner == request.user:
            return True
        return False


class IsAdmin(BasePermission):
    """Проверяет, является ли пользователь админом."""

    def has_permission(self, request, view):
        if request.user.is_superuser:
            return True
        return False
