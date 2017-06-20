from django.db import models
from autoslug import AutoSlugField
from usuarios.models import Usuario
from pacotes.models import Pacote

class Evento(models.Model):
    nome = models.CharField('Nome do evento', max_length=200)
    quantidade_pessoas = models.PositiveIntegerField('Quantidade de pessoas')
    data = models.DateTimeField('Data do evento')
    RESTRICOES = (('vegetariano', 'Vegetariano'),
                  ('regional', 'Regional'))
    restricoes = models.CharField('Tipos de alimentos', choices=RESTRICOES, max_length = 50, null=True, blank=True)
    orcamento = models.FloatField('Orçamento para o evento')
    descricao = models.CharField('Descrição', max_length=400, blank=True)
    slug = AutoSlugField('Slug', populate_from='nome', always_update=True, unique_with=('data'), unique=True)
    criador = models.ForeignKey(Usuario, verbose_name = 'Criador', related_name = 'eventos')
    entregue = models.BooleanField('Pacote entregue ao evento', default=False)

    pacotes = models.ManyToManyField(Pacote, verbose_name='Pacotes do evento', related_name = 'pacotes')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return str(self.nome) or str(self.cpf_cnpj) or str(self.email)

class Endereco(models.Model):
    rua = models.CharField('Rua', max_length = 250)
    bairro = models.CharField('Bairro', max_length = 100)
    cidade = models.CharField('Cidade', max_length = 50)
    estado = models.CharField('Estado', max_length = 20)
    cep = models.CharField('CEP', max_length = 15)
    numero = models.CharField('Número', max_length = 10)
    evento = models.OneToOneField(Evento, verbose_name='Local do evento', related_name = 'endereco', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Endereço'
        verbose_name_plural = 'Endereços'