from rest_framework import permissions

USER = 'user'
MODERATOR = 'moderator'
ADMIN = 'admin'


class AdminOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        return request.user.role == ADMIN or request.user.is_superuser


class MeOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_anonymous:
            return False
        else:
            return True


class GetAllPostDeleteAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        elif request.user.is_anonymous:
            return False
        return (request.user.role == ADMIN or request.user.is_superuser)


class ReviewCommentsPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.user.is_anonymous:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method == 'GET':
            return True
        return (
                (request.method == 'PATCH' and obj.author == request.user)
                or request.user.role == ADMIN
                or request.user.role == MODERATOR
                or request.user.is_superuser
        )
