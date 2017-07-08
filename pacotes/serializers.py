from rest_framework import serializers, fields
from .models import Item, Pacote, ItemPacote, MY_CHOICES


class ItemSerializer(serializers.ModelSerializer):

    categorias = fields.MultipleChoiceField(choices=MY_CHOICES)

    class Meta:
        model = Item
        fields = ('id', 'slug', 'nome','preco','descricao','categorias')
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
