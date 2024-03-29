from rest_framework import serializers

from .models import Evento, Endereco

class EventoSerializer(serializers.ModelSerializer):
    # endereco = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = ('slug', 'nome','quantidade_pessoas','data','orcamento','descricao','criador','entregue','pacotes','endereco','status','codigo_pag_seguro')
        read_only_fields = ('slug','criador','entregue','pacotes','endereco','codigo_pag_seguro')

class EventoAtualizaStatusSerializer(serializers.ModelSerializer):
    # endereco = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Evento
        fields = ('status',)

class EventoPacoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = ('slug','pacotes')
        read_only_fields = ('slug',)

    def update(self, instance, validated_data):
        serializers.raise_errors_on_nested_writes('update', self, validated_data)
        for pacote in validated_data['pacotes']: 
            instance.pacotes.add(pacote)
        return instance

class EventoRemoverPacoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Evento
        fields = ('slug','pacotes')
        read_only_fields = ('slug',)

    def update(self, instance, validated_data):
        serializers.raise_errors_on_nested_writes('update', self, validated_data)
        for pacote in validated_data['pacotes']: 
            instance.pacotes.remove(pacote)
        return instance

class PacotesEventoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Evento
        fields = ('slug','pacotes')
        read_only_fields = ('slug',)

class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = ('id','rua','bairro','cidade','estado','cep','numero', 'evento')
        read_only_fields = ('id', 'evento')

class EnderecoCreateSerializer(EnderecoSerializer):

	class Meta:
		model = Endereco
		fields = ('rua','bairro','cidade','estado','cep','numero')