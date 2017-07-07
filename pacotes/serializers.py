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
        fields = ('id','slug', 'nome','quantidade_pessoas','preco','dono','codigo')
        read_only_fields = ('id','slug')

class ItemPacoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemPacote
        fields = ('slug', 'item','quantidade_item','pacote')
        read_only_fields = ('slug',)
