from rest_framework.permissions import IsAuthenticated


class IsAuthorPermission(IsAuthenticated):
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user
