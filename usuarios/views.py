from rest_framework import viewsets
from .models import FornecedorBuffet, Contratante
from .serializers import FornecedorBuffetSerializer, FornecedorBuffetCreateSerializer, ContratanteSerializer, ContratanteCreateSerializer
from .permissions import UsuarioPermission
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
