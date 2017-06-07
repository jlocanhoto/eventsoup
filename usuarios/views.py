from django.shortcuts import get_object_or_404

from rest_framework import viewsets

from .models import FornecedorBuffet, Contratante, Endereco
from .serializers import FornecedorBuffetSerializer, FornecedorBuffetCreateSerializer, ContratanteSerializer, ContratanteCreateSerializer, EnderecoSerializer, EnderecoCreateSerializer
from .permissions import UsuarioPermission, EnderecoPermission
from .models import Usuario

class FornecedorBuffetViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    queryset = FornecedorBuffet.objects.all()
    serializer_class = FornecedorBuffetSerializer
    permission_classes = [UsuarioPermission]

    def get_serializer_class(self):
        serializer_class = super(FornecedorBuffetViewSet, self).get_serializer_class()
        if self.request.method == 'POST':
            serializer_class = FornecedorBuffetCreateSerializer

        return serializer_class

class ContratanteViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    queryset = Contratante.objects.all()
    serializer_class = ContratanteSerializer
    permission_classes = [UsuarioPermission]

    def get_serializer_class(self):
        serializer_class = super(ContratanteViewSet, self).get_serializer_class()
        if self.request.method == 'POST':
            serializer_class = ContratanteCreateSerializer

        return serializer_class

class EnderecoViewSet(viewsets.ModelViewSet):

    lookup_field = 'id'
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [EnderecoPermission]

    def get_queryset(self):
        return self.request.user.endereco.all()

    def perform_create(self, serializer):
        """
        utilizado para adicionar o usuário que criou o endereco
        """
        serializer.save(usuario=self.request.user)

    def get_serializer_class(self):
        serializer_class = super(EnderecoViewSet, self).get_serializer_class()
        if self.request.method in ('PUT','POST'):
            serializer_class = EnderecoCreateSerializer

        return serializer_class
