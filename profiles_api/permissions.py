from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit their own profile"""

    # This function will be called every time when HTTP request is
    # made to the API the permission is assigned to.
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit their own profile"""

        # If the HTTP request method is SAFE_METHOD i.e
        # it does not change the object (LIST or CREATE Objects) return True.
        if request.method in permissions.SAFE_METHODS:
            return True

        # Else, allow only if requested user id is same objects user id.
        return obj.id == request.user.id  # True;


class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, obj):
        """Check the user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.user_profile.id == request.user.id
