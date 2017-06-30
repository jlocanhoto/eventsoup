from rest_framework import serializers
from .models import Item, Pacote, ItemPacote


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'slug', 'nome','preco','descricao')
        read_only_fields = ('id', 'slug')

class PacoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pacote
        fields = ('id','slug', 'nome','quantidade_pessoas','restricoes','preco','dono','codigo','codigo_pag_seguro')
        read_only_fields = ('id','slug')

class ItemPacoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemPacote
        fields = ('slug', 'item','quantidade_item','pacote')
        read_only_fields = ('slug',)
