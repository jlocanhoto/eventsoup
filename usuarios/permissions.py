
from rest_framework.permissions import BasePermission

class UsuarioPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method == 'POST':
            return True
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if request.method in ('PUT', 'DELETE','PATCH'):
            return request.user and (request.user.is_staff or request.user.cpf_cnpj == view.get_object().cpf_cnpj)
        return False
