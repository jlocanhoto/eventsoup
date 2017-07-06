from rest_framework import serializers

from .models import FornecedorBuffet, Contratante, Endereco

class FornecedorBuffetSerializer(serializers.ModelSerializer):
    endereco = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = FornecedorBuffet
        fields = ('id','slug', 'nome','email','telefone','celular','cpf_cnpj','faz_entrega','endereco')
        read_only_fields = ('id','slug','endereco')

class FornecedorBuffetCreateSerializer(serializers.ModelSerializer):
    password1 = serializers.CharField(label='Senha', write_only=True)
    password2 = serializers.CharField(label='Confirmar Senha', write_only=True)


    def validate(self, attrs):
        if attrs.get('password1','') == '':
            raise serializers.ValidationError({'password1': 'A senha esta vazia'})
        if attrs.get('password2','') == '':
            raise serializers.ValidationError({'password2': 'A confirmação de senha esta vazia'})

        if attrs.get('password1','') != attrs.get('password2',''):
            raise serializers.ValidationError({'password2': 'A confirmação de senha é diferente da senha'})
        return attrs

    def create(self, validated_data):
        senha = validated_data.get('password1','')
        validated_data.pop('password1')
        validated_data.pop('password2')
        instance = super(FornecedorBuffetCreateSerializer, self).create(validated_data)
        instance.set_password(senha)
        instance.save()
        return instance

    class Meta:
        model = FornecedorBuffet
        fields = ('nome','email','telefone','celular','cpf_cnpj','faz_entrega', 'password1', 'password2')

class ContratanteSerializer(serializers.ModelSerializer):
    endereco = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Contratante
        fields = ('id','slug', 'nome','email','telefone','celular','cpf_cnpj','endereco')
        read_only_fields = ('id','slug','endereco')

class ContratanteCreateSerializer(FornecedorBuffetCreateSerializer):

    class Meta:
        model = Contratante
        fields = ('nome','email','telefone','celular','cpf_cnpj', 'password1', 'password2')

class EnderecoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Endereco
        fields = ('id','rua','bairro','cidade','estado','cep','numero', 'usuario')
        read_only_fields = ('id',)

class EnderecoCreateSerializer(EnderecoSerializer):

    class Meta:
        model = Endereco
        fields = ('rua','bairro','cidade','estado','cep','numero')