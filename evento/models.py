from django.db import models
from autoslug import AutoSlugField
from usuarios.models import Usuario

class Evento(models.Model):
    nome = models.CharField('Evento', max_length=200)
    quantidade_pessoas = models.PositiveIntegerField('Quantidade de Pessoas')
    data = models.DateTimeField('Data do Evento')
    local = models.CharField('Local do Evento', max_length = 200)
    RESTRICOES = (('vegetariano', 'Vegetariano'),
                  ('regional', 'Regional'))
    restricoes = models.CharField('Tipos de Alimentos', choices=RESTRICOES, max_length = 50)
    orcamento = models.FloatField('Orçamento para o Evento')
    slug = AutoSlugField('Slug', populate_from='nome', unique_with=('data'), unique=True)
    criador = models.ForeignKey(Usuario, verbose_name = 'Criador', related_name = 'eventos')

    class Meta:
        verbose_name = 'Evento'
        verbose_name_plural = 'Eventos'

    def __str__(self):
        return str(self.nome) or str(self.cpf_cnpj) or str(self.email)
