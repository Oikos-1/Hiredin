from rest_framework.permissions import BasePermission
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.exceptions import AuthenticationFailed


class BasePermissionRole(BasePermission):
    required_role = None
    def has_permission(self, request, view):
        try:
            user_auth = JWTAuthentication().authenticate(request)
            if user_auth:
                user, _ = user_auth
                return user.role == self.required_role
        except AuthenticationFailed:
            return False
        return False
    
class IsEmployee(BasePermissionRole):
    required_role = 'employee'

class  IsEmployer(BasePermissionRole):
    required_role = 'employer'
