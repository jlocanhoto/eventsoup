from rest_framework.permissions import BasePermission
from .models import Pacote

from usuarios.models import FornecedorBuffet

class ItemPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method == 'POST':
            # print(isinstance(request.user, FornecedorBuffet))
            return request.user and request.user.is_authenticated
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if request.method in ('PUT', 'DELETE','PATCH'):
            try:
                return request.user and (request.user.is_staff or request.user.cpf_cnpj == view.get_object().criador.cpf_cnpj)
            except:
                return False
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
            try:
                return request.user and (request.user.is_staff or request.user.cpf_cnpj == view.get_object().dono.cpf_cnpj)
            except:
                return False
        return False

class ItemPacotePermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method in ('POST'):
            try:
                pacote = Pacote.objects.get(slug=view.kwargs['slug_pacote'])
                return request.user and (request.user.is_staff or request.user.cpf_cnpj == pacote.dono.cpf_cnpj)
            except:
                return False
        if request.method in ('GET', 'HEAD', 'OPTIONS'):
            return True
        if request.method in ('PUT', 'DELETE','PATCH'):
            try:
                return request.user and (request.user.is_staff or request.user.cpf_cnpj == view.get_object().pacote.dono.cpf_cnpj)
            except:
                return False
        return False
