from django.shortcuts import get_object_or_404
from django.http import Http404, JsonResponse

from rest_framework import viewsets
from rest_framework.generics import ListAPIView, UpdateAPIView, RetrieveAPIView, GenericAPIView
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Evento, Endereco
from .serializers import EventoSerializer, EventoPacoteSerializer, EventoRemoverPacoteSerializer, PacotesEventoSerializer, EnderecoSerializer, EnderecoCreateSerializer, EventoAtualizaStatusSerializer
from .permissions import EventoPermission, ProximosEventosPermission, EnderecoPermission

from pacotes.serializers import PacoteSerializer, ItemPacoteSerializer
from pacotes.views import GeradorCodigo
from pacotes.models import Item

from django.db import transaction

from datetime import datetime

class EventoViewSet(viewsets.ModelViewSet):

    lookup_field = 'slug'
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [EventoPermission]

    @transaction.atomic
    def create(self, request, *args, **kwargs):
        """
        utilizado para adicionar os pacotes e os itens ao evento;
        e o fornecedor do pacote como dono do pacote;
        e o usuário logado como o criador do evento.
        """
        sid = transaction.savepoint() # salva ponto da transação, caso ocorrer algum erro abaixo
        evento_dict = request.data
        pacote_dict = request.data['pacotes']
        itens_dict = pacote_dict['itens']
        endereco_dict = request.data['endereco']

        evento_dict.pop('pacotes')
        evento_dict.pop('endereco')

        i = []

        try:
            pacote_dict['dono'] = pacote_dict['fornecedor']

            pacote_dict['codigo'] = GeradorCodigo.codigo_pedido(pacote_dict['fornecedor'])
            # pacote_dict['codigo_pag_seguro'] = GeradorCodigo.codigo_pag_seguro()        

            pacote_dict.pop('fornecedor')
            pacote_dict.pop('itens')
            # print("AAA")
            pacote = PacoteSerializer(data=pacote_dict)
            
            if pacote.is_valid():
                pacote = pacote.save()
                
                itens = []
                for item in itens_dict:
                    try:
                        item_aux = get_object_or_404(Item, id=item['id'])
                        
                        item['item'] = item_aux.id
                        item['pacote'] = pacote.id
                        item.pop('id')
                        item_salvo = ItemPacoteSerializer(data=item)
                        
                        if item_salvo.is_valid():
                            itens.append(item_salvo)
                        else:
                            raise Exception()
                            
                    except Http404:
                        transaction.savepoint_rollback(sid) # deleta o pacote caso o item solicitado nao for encontrado
                        return Response({'message': 'Item não encontrado', 'item': item['id']}, status=404)
                    except Exception:
                        transaction.savepoint_rollback(sid) # deleta o pacote caso houver algum erro com o item
                        return Response({'message': 'Erro em Item', 'item': item['id']}, status=404)
                    
                for item in itens:
                    if item.is_valid():
                        it = item.save()
                        i.append(it)
            else:
                transaction.savepoint_rollback(sid)
                return Response({'message': 'Erro no pacote'}, status=400)

        except Http404:
            transaction.savepoint_rollback(sid) # deleta qualquer inserção da transição caso houver algum erro 404
            return Response({'message': 'Fornecedor não encontrado'}, status=404)
        except Exception:
            transaction.savepoint_rollback(sid) # deleta qualquer inserção da transição caso houver algum erro
            return Response({'message': 'Erro na criação'}, status=400)

        endereco = EnderecoSerializer(data=endereco_dict)
        serializer = EventoSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer = serializer.save(criador=self.request.user, codigo_pag_seguro=request.data['codigo_pag_seguro'])
            serializer.pacotes.add(pacote)
            if endereco.is_valid():
                endereco.save(evento=serializer)
            else:
                transaction.savepoint_rollback(sid)
                return Response({'message': 'Erro no endereco'}, status=400)
            
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=201, headers=headers)
        else:
            print(serializer.errors)
            transaction.savepoint_rollback(sid)
            return Response({'message': 'Erro na criação'}, status=400)

    def list(self, request, *args, **kwargs):
        try:
            # print("eventos")
            # ordenado por data (TODOS OS EVENTOS)
            eventos = Evento.objects.filter(criador=self.request.user).filter(data__lte=datetime.now()).order_by('-data')
            return montar_json_eventos(eventos)
        except:
            return Response({'message': 'erro'}, status=400)

class ProximosEventos(ListAPIView):
    permission_classes = [ProximosEventosPermission]
    serializer_class = EventoSerializer
    model = Evento
    queryset = Evento.objects.all()

    def list(self, request, *args, **kwargs):
        try:
            # ordenado por data (APENAS OS EVENTOS APÓS A DATA ATUAL .now())
            eventos = self.request.user.eventos.all().filter(data__gte=datetime.now()).order_by('data')
            return montar_json_eventos(eventos)
        except:
            return Response({'message': 'erro'}, status=400)

def montar_json_eventos(eventos):
    if len(eventos) > 0:
        content = []
        for evento in eventos:
            content.append(evento.as_json())
        return Response(content)
    else:
        return Response({'message': 'Nenhum evento encontrado.'}, status=400)

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

    def list(self, request, *args, **kwargs):
        evento = get_object_or_404(Evento, slug=self.kwargs.get('slug',''))
        content = [p.as_json() for p in evento.pacotes.all()]
        return Response(content)

class ConfirmaEntregaEvento(APIView):

    def post(self, request):
        slug_evento = request.data['slug_evento']
        cpf_cnpj_inicio = request.data['tres_digitos_cpf_cnpj']
        content = {}
        status=400
        if len(cpf_cnpj_inicio) == 3:
            evento = get_object_or_404(Evento, slug=slug_evento)

            if evento.entregue == False:
                if evento.criador.cpf_cnpj.startswith(cpf_cnpj_inicio):
                    content = {'entregue': True, 'message': 'Evento entregue'}
                    status = 200
                    evento.entregue = True
                    evento.save()
                else:
                    content = {'entregue': False, 'message': 'CPF incorreto'}
            else:
                content = {'entregue': True, 'message': 'Evento já entregue'}

            # analisar se precisa persistir no banco a validação da "entrega" do pacote ao evento

            return Response(content, status=status)

        else:
            return Response({'message': 'Deve ser os três primeiros dígitos do CPF'}, status=status)



class EventoAtualizaStatus(UpdateAPIView):

    lookup_field = 'slug'
    model = Evento
    # queryset = Evento.objects.all()
    serializer_class = EventoAtualizaStatusSerializer
    permission_classes = [EventoPermission]

    def get_object(self):
        
        return get_object_or_404(Evento, slug=self.kwargs.get('slug',''))