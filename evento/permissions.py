from rest_framework.permissions import BasePermission

from .models import Evento

class EventoPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method == 'POST':
            return request.user and request.user.is_authenticated
        if request.method in ('GET','HEAD','OPTIONS'):
            return True
        if request.method in ('PUT', 'DELETE','PATCH'):
            try:
                return request.user and (request.user.is_staff or request.user.cpf_cnpj == view.get_object().criador.cpf_cnpj)
            except:
                return False
        return False

class ListOwnerEventosPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated

class EnderecoPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_staff:
            return True
        if request.method in ('POST','GET','HEAD','OPTIONS'):
            try:
                evento = Evento.objects.get(slug=view.kwargs['slug_evento'])
                print(evento.criador.cpf_cnpj == request.user.cpf_cnpj)
                return request.user and (request.user.is_staff or request.user.cpf_cnpj == evento.criador.cpf_cnpj)
            except:
                return False
        if request.method in ('PUT','DELETE','PATCH'):
            try:
                return request.user and (request.user.is_staff or request.user.cpf_cnpj == view.get_object().evento.criador.cpf_cnpj)
            except:
                return False
        return False
