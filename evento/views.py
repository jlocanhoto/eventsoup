from rest_framework import viewsets
from rest_framework.generics import ListAPIView
from .models import Evento
from .serializers import EventoSerializer
from .permissions import EventoPermission, ListOwnerEventosPermission

class EventoViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [EventoPermission]

    def perform_create(self, serializer):
        """
        utilizado para adicionar o usuário que criou o evento como criador do evento
        """
        serializer.save(criador=self.request.user)

class ListOwnerEventos(ListAPIView):
    permission_classes = [ListOwnerEventosPermission]
    serializer_class = EventoSerializer
    model = Evento
    queryset = Evento.objects.all()

    def get_queryset(self):
        return self.request.user.eventos.all()
