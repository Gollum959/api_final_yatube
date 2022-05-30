from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """Permissions SAFE_METHODS for everybody, others for authors."""

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
