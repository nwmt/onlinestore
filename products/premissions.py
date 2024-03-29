from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user_id == request.user.id or request.user.is_staff


class IsOrderCreator(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.user_id == request.user.id or request.user.is_staff
