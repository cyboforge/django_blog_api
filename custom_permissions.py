from rest_framework import permissions

class IsSelfOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow users to edit their own user objects.
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD or OPTIONS requests (read-only)
        if request.method == 'POST':
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the user is the owner of the object
        return obj == request.user

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow users to edit their own user objects.
    """

    def has_object_permission(self, request, view, obj):
        # Allow GET, HEAD or OPTIONS requests (read-only)
        if request.method == 'POST':
            return True
        elif request.method in permissions.SAFE_METHODS:
            return True
        
        # Check if the user is the owner of the object
        return obj.created_by == request.user
