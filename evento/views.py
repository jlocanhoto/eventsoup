from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, GenericAPIView

from .models import Evento, Endereco
from .serializers import EventoSerializer, EventoPacoteSerializer, EventoRemoverPacoteSerializer, PacotesEventoSerializer, EnderecoSerializer, EnderecoCreateSerializer
from .permissions import EventoPermission, ListOwnerEventosPermission, EnderecoPermission

from pacotes.serializers import PacoteSerializer

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

    def get_queryset(self):
        return Evento.objects.filter(criador=self.request.user)

class ListOwnerEventos(ListAPIView):
    permission_classes = [ListOwnerEventosPermission]
    serializer_class = EventoSerializer
    model = Evento
    queryset = Evento.objects.all()

    def get_queryset(self):
        return self.request.user.eventos.all()

class EnderecoViewSet(viewsets.ModelViewSet):

    lookup_field = 'id'
    queryset = Endereco.objects.all()
    serializer_class = EnderecoSerializer
    permission_classes = [EnderecoPermission]

    def get_queryset(self):
        evento = get_object_or_404(Evento, slug=self.kwargs.get('slug_evento',''))
        return Endereco.objects.filter(evento=evento)

    def perform_create(self, serializer):
        """
        utilizado para adicionar o usuário que criou o endereco
        """
        evento = get_object_or_404(Evento, slug=self.kwargs.get('slug_evento',''))
        serializer.save(evento=evento)

    def get_serializer_class(self):
        serializer_class = super(EnderecoViewSet, self).get_serializer_class()
        if self.request.method in ('PUT','POST'):
            serializer_class = EnderecoCreateSerializer

        return serializer_class

class EventoPacote(UpdateAPIView):

    lookup_field = 'slug'
    model = Evento
    # queryset = Evento.objects.all()
    serializer_class = EventoPacoteSerializer
    permission_classes = [EventoPermission]

    def get_object(self):
        
        return get_object_or_404(Evento, slug=self.kwargs.get('slug',''))

class EventoRemoverPacote(UpdateAPIView, RetrieveAPIView, GenericAPIView):

    lookup_field = 'slug'
    model = Evento
    serializer_class = EventoRemoverPacoteSerializer
    permission_classes = [EventoPermission]

    def get_object(self):        
        return get_object_or_404(Evento, slug=self.kwargs.get('slug',''))

class PacotesEvento(ListAPIView):
    model = Evento
    serializer_class = PacoteSerializer
    permission_classes = [EventoPermission]

    def get_queryset(self):
        evento = get_object_or_404(Evento, slug=self.kwargs.get('slug',''))
        return evento.pacotes.all()