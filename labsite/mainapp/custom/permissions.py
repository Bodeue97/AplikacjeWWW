from rest_framework.permissions import BasePermission
class CanViewOsoba(BasePermission):
    def has_permission(self, request, view):
        return request.user.has_perm('mainapp.view_osoba')


class CanViewOtherPersons(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.user.has_perm('your_app.can_view_other_persons'):
            return True
        return obj.wlasciciel == request.user