from rest_framework import serializers
from .models import Evento


class EventoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = ('slug', 'nome','quantidade_pessoas','data','local','restricoes','orcamento','criador')
        read_only_fields = ('slug','criador')
