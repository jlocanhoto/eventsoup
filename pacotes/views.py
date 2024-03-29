from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

from .models import Item, Pacote, ItemPacote, MY_CHOICES
from .serializers import ItemSerializer, PacoteSerializer, ItemPacoteSerializer
from .permissions import ItemPermission, PacotePermission, ItemPacotePermission

from usuarios.models import FornecedorBuffet

import hashlib
from datetime import datetime

import random

class ItemViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [ItemPermission]

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Item.objects.all()
            
        return Item.objects.filter(criador=self.request.user)

    def perform_create(self, serializer):
        """
        utilizado para adicionar o usuário que criou o evento como criador do evento
        """
        serializer.save(criador=self.request.user)

class PacoteViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    queryset = Pacote.objects.all()
    serializer_class = PacoteSerializer
    permission_classes = [PacotePermission]

    def perform_create(self, serializer):
        """
        utilizado para adicionar o usuário que criou o evento como criador do evento
        """
        valid = True
        code = ''
        code_pag_seguro = ''

        while valid:
            code = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVXWYZ') for i in range(4))
            pacote = Pacote.objects.filter(dono=self.request.user).filter(codigo=code)

            if len(pacote) == 0:
                valid = False

        code_pag_seguro = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ') for i in range(32))
        code_pag_seguro = code_pag_seguro + str(datetime.now())  
        code_pag_seguro = code_pag_seguro.encode('utf-8')
        code_pag_seguro = hashlib.md5(code_pag_seguro).hexdigest()

        serializer.save(dono=self.request.user, codigo=code, codigo_pag_seguro=code_pag_seguro)

class ItemPacoteViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    queryset = ItemPacote.objects.all()
    serializer_class = ItemPacoteSerializer
    permission_classes = [ItemPacotePermission]

    def get_queryset(self):
        """
        utilizado para retornar apenas os itens e quantidade deste item do pacote
        informado na url
        """
        pacote = get_object_or_404(Pacote, slug=self.kwargs.get('slug_pacote',''))
        if self.request.user.is_superuser:
            return ItemPacote.objects.all()

        return ItemPacote.objects.filter(pacote=pacote)

    def perform_create(self, serializer):
        """
        utilizado para adicionar o item criado ao pacote informado na url
        """
        pacote = get_object_or_404(Pacote, slug=self.kwargs.get('slug_pacote',''))
        serializer.save(pacote=pacote)

class ListPacotes(ListAPIView):
    permission_classes = [PacotePermission]
    serializer_class = PacoteSerializer
    model = Pacote
    queryset = Pacote.objects.all()

    # lista todos os pacotes do fornecedor, ordenador pela data do evento, independente de estar pago
    def list(self, request, *args, **kwargs): 
        content = []
        eventos = eventos_dos_pacotes(self)

        if len(eventos) > 0:
            eventos.sort(key=lambda x: x.data, reverse=False) # eventos ordenados por data de acontecimento
            content = montar_json_pacotes(self, eventos)

        return Response(content)

class AllPacotes(APIView):

    # retorna os pacotes do fornecedor ordenados por data do evento, se pagos e não entregues
    def get(self, request):        
        content = []
        eventos = eventos_dos_pacotes(self)
        
        if len(eventos) > 0:
            eventos.sort(key=lambda x: x.data, reverse=False) # eventos ordenados por data de acontecimento
            eventos = list(filter(lambda x: (x.status=="Paga" and x.entregue==False), eventos))
            content = montar_json_pacotes(self, eventos)

        return Response(content)

def eventos_dos_pacotes(self):
    eventos = []

    if self.request.user.is_superuser:
        pacotes = Pacote.objects.all()
    else:
        pacotes = Pacote.objects.filter(dono=self.request.user)

    for pacote in pacotes:
        try:
            evento = pacote.pacotes.get()
            eventos.append(evento)
        except:
            pass

    return eventos

def montar_json_pacotes(self, eventos):
    content = []
    for evento in eventos:
        try:
            endereco = evento.endereco.as_json()
        except:
            endereco = 'não informado'
        content_i = {
                        'evento': {
                            'nome': evento.nome,                                        
                            'data': evento.data,
                            'entregue': evento.entregue,
                            'status_pagamento': evento.status,
                            'endereco': endereco
                        },
                        'pacotes': [pacote.as_json() for pacote in evento.pacotes.all() if pacote.dono==self.request.user]
                    }
        content.append(content_i)
    return content

class PacoteSelecionado(APIView):
    
    def get(self, request, slug):
        pacote = get_object_or_404(Pacote, slug=slug)

        return Response(pacote.as_json())

class PacotesDefault(APIView):
    # agrupar pacotes por categorias de itens
    def get(self, request):
        fornecedores = FornecedorBuffet.objects.all()
        content = []
        for fornecedor in fornecedores:
            pacotes = []
            for choices in MY_CHOICES:
                try:
                    print(choices[1].lower())
                    choice = fornecedor.itens.filter(categorias__contains=choices[1].lower())
                    # print([item.categorias for item in choice])
                    if len(choice) > 0:
                        d = {choices[1]: [item.as_json() for item in choice]}
                        pacotes.append(d)
                except:
                    print("erro na busca por itens do fornecedor %d" %fornecedor.id)
            if len(pacotes) > 0:
                d = {
                    'fornecedor': fornecedor.id,
                    'pacotes': pacotes
                }
                content.append(d)
        
        return Response(content)

class LazyEncoder(DjangoJSONEncoder):
    def default(self, obj):
        if isinstance(obj, YourCustomType):
            return force_text(obj)
        return super(LazyEncoder, self).default(obj)

class GeradorCodigo():
    def codigo_pedido(fornecedor):
        valid = True
        code = ''
        while valid:
            code = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ') for i in range(4))
            pacote = Pacote.objects.filter(dono_id=fornecedor).filter(codigo=code)
            
            if len(pacote) == 0:
                valid = False
        return code

    def codigo_pag_seguro():
        code = ''.join(random.choice('0123456789abcdefghijklmnopqrstuvxwyzABCDEFGHIJKLMNOPQRSTUVXWYZ') for i in range(32))
        code = code + str(datetime.now())  
        code = code.encode('utf-8')
        code = hashlib.md5(code).hexdigest()

        return code