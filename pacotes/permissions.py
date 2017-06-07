from rest_framework.permissions import BasePermission

class ItemPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if request.method in ('PUT', 'DELETE','PATCH'):
            return request.user and (request.user.is_staff or request.user.cpf_cnpj == view.get_object().criador.cpf_cnpj)
        return False

class PacotePermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if request.method in ('PUT', 'DELETE','PATCH'):
            return request.user and (request.user.is_staff or request.user.cpf_cnpj == view.get_object().dono.cpf_cnpj)
        return False

class ItemPacotePermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if request.method in ('PUT', 'DELETE','PATCH','POST'):
            return request.user and (request.user.is_staff or request.user.cpf_cnpj == view.pacote.dono.cpf_cnpj)
        return False