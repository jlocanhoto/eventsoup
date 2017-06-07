from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.generics import ListAPIView
from .models import Item, Pacote, ItemPacote
from .serializers import ItemSerializer, PacoteSerializer, ItemPacoteSerializer
from .permissions import ItemPermission, PacotePermission, ItemPacotePermission

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
        serializer.save(dono=self.request.user)

class ItemPacoteViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    queryset = ItemPacote.objects.all()
    serializer_class = ItemPacoteSerializer
    permission_classes = [ItemPacotePermission]

    def dispatch(self, request, *args, **kwargs):
        self.pacote = get_object_or_404(Pacote, slug=kwargs.get('slug_produto',''))
        return super(ItemPacoteViewSet, self).dispatch(request, args, kwargs)

    def get_queryset(self):
        """
        utilizado para retornar apenas os itens e quantidade deste item do pacote
        informado na url
        """
        return ItemPacote.objects.filter(pacote=self.pacote)

    def perform_create(self, serializer):
        """
        utilizado para adicionar o item criado ao pacote informado na url
        """
        serializer.save(pacote=self.pacote)