from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Evento, Endereco
from .serializers import EventoSerializer, EventoPacoteSerializer, EventoRemoverPacoteSerializer, PacotesEventoSerializer, EnderecoSerializer, EnderecoCreateSerializer, EventoAtualizaEstatusSerializer
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
        try:
            return Evento.objects.filter(criador=self.request.user)
        except:
            return []

class ListOwnerEventos(ListAPIView):
    permission_classes = [ListOwnerEventosPermission]
    serializer_class = EventoSerializer
    model = Evento
    queryset = Evento.objects.all()

    def get_queryset(self):
        try:
            return self.request.user.eventos.all()
        except:
            return []

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

class ConfirmaEntregaEvento(APIView):

    def post(self, request):
        slug_evento = request.data['slug_evento']
        cpf_cnpj_inicio = request.data['tres_digitos_cpf_cnpj']

        if len(cpf_cnpj_inicio) == 3:
            evento = evento = get_object_or_404(Evento, slug=slug_evento)

            if evento.entregue == False:
                if evento.criador.cpf_cnpj.startswith(cpf_cnpj_inicio):
                    content = {'entregue': True, 'message': 'Event delivered'}
                    evento.entregue = True
                    evento.save()
                else:
                    content = {'entregue': False, 'message': 'Incorrect CPF'}
            else:
                content = {'entregue': True, 'message': 'Event already delivered'}

            # analisar se precisa persistir no banco a validação da "entrega" do pacote ao evento

            return Response(content)

        else:
            return Response({'message': 'Must be the first three numbers of the CPF'}, status=400)



class EventoAtualizaEstatus(UpdateAPIView):

    lookup_field = 'slug'
    model = Evento
    # queryset = Evento.objects.all()
    serializer_class = EventoAtualizaEstatusSerializer
    permission_classes = [EventoPermission]

    def get_object(self):
        
        return get_object_or_404(Evento, slug=self.kwargs.get('slug',''))