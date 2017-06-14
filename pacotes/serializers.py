from rest_framework import serializers
from .models import Item, Pacote, ItemPacote


class ItemSerializer(serializers.ModelSerializer):

    class Meta:
        model = Item
        fields = ('id', 'slug', 'nome')
        read_only_fields = ('id', 'slug')

class PacoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Pacote
        fields = ('id','slug', 'nome','quantidade_pessoas','restricoes','preco','dono')
        read_only_fields = ('id','slug','dono')

class ItemPacoteSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemPacote
        fields = ('slug', 'item','quantidade_item','pacote')
        read_only_fields = ('slug','pacote')
