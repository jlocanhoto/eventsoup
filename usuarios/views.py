from rest_framework import viewsets
from .models import FornecedorBuffer, Contratante
from .serializers import FornecedorBufferSerializer, FornecedorBufferCreateSerializer, ContratanteSerializer, ContratanteCreateSerializer
from .permissions import UsuarioPermission

class FornecedorBufferViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    queryset = FornecedorBuffer.objects.all()
    serializer_class = FornecedorBufferSerializer
    permission_classes = [UsuarioPermission]

    def get_serializer_class(self):
        serializer_class = super(FornecedorBufferViewSet, self).get_serializer_class()
        if self.request.method == 'POST':
            serializer_class = FornecedorBufferCreateSerializer

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
