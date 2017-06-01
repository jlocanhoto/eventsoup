from rest_framework import serializers

from .models import FornecedorBuffet, Contratante

class FornecedorBuffetSerializer(serializers.ModelSerializer):
    class Meta:
        model = FornecedorBuffet
        fields = ('slug', 'nome','email','telefone','cpf_cnpj','endereco','faz_entrega')
        read_only_fields = ('slug',)

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
        fields = ('nome','email','telefone','cpf_cnpj','endereco','faz_entrega', 'password1', 'password2')

class ContratanteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Contratante
        fields = ('slug', 'nome','email','telefone','cpf_cnpj','endereco')
        read_only_fields = ('slug',)

class ContratanteCreateSerializer(FornecedorBuffetCreateSerializer):

    class Meta:
        model = Contratante
        fields = ('nome','email','telefone','cpf_cnpj','endereco', 'password1', 'password2')
