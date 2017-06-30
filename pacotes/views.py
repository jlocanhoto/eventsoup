from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from django.utils.encoding import force_text
from django.core.serializers.json import DjangoJSONEncoder
from django.core.serializers import serialize

from .models import Item, Pacote, ItemPacote
from .serializers import ItemSerializer, PacoteSerializer, ItemPacoteSerializer
from .permissions import ItemPermission, PacotePermission, ItemPacotePermission

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

class PacoteSelecionado(APIView):
    
    def get(self, request, slug):
        pacote = get_object_or_404(Pacote, slug=slug)
        item_pacotes = ItemPacote.objects.filter(pacote=pacote)

        lista = [x.item.as_json() for x in item_pacotes]
        
        content = {'code': pacote.codigo, 'itens': lista}

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