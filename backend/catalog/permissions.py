from rest_framework import permissions
from users.models import ProfileType

class IsProfileLibrarian(permissions.BasePermission):
    """ Permite acesso apenas se o usuário tiver profile_type com o nome "Librarian" """

    def has_permission(self, request, view):
        if not request.user or not request.user.is_authenticated:
            return False

        profile = getattr(request.user, 'profile_type', None)
        return (
            profile is not None and 
            profile.name == ProfileType.Type.LIBRARIAN
        )