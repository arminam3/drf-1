from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsSuperUser(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_superuser)
    
class IsStaffOrReadOnly(BasePermission):
    """
    Return True if user is_staff, otherwise False
    """
    def has_permission(self, request, view):
        return bool(
                request.method in SAFE_METHODS or
                request.user and
                request.user.is_staff
                )

class IsSuperUserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.method in SAFE_METHODS and 
            request.user.is_staff or
            request.user and 
            request.user.is_superuser 
        )
    
class IsAuthorOrReadOnly(BasePermission):
    def has_object_permission(self, request, view, obj):
        return bool(
            request.method in SAFE_METHODS or
            #get access to author of object            
            request.user == obj.author or
            #get access to superuser
            request.user.is_authenticated and request.user.is_superuser
        )
    
class IsSuperuserOrStaffReadOnly(BasePermission):
    def has_permission(self, request, view):
        return bool(
            request.user.is_superuser or
            request.method in SAFE_METHODS and 
            request.user.is_authenticated and
            request.user.is_staff
        )

