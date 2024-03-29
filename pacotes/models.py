from django.db import models
from autoslug import AutoSlugField
from usuarios.models import Usuario

from multiselectfield import MultiSelectField

MY_CHOICES = (('expresso', 'Expresso'),
              ('casual', 'Casual'),
              ('festa', 'Festa'))

class Pacote(models.Model):
    nome = models.CharField('Nome do Pacote', max_length=200)
    quantidade_pessoas = models.PositiveIntegerField('Quantidade de Pessoas')
    # RESTRICOES = (('vegetariano', 'Vegetariano'),
                #   ('regional', 'Regional'))
    # restricoes = models.CharField('Tipo do Pacote', choices=RESTRICOES, max_length = 50)
    preco = models.FloatField('Preço do Pacote')
    slug = AutoSlugField('Slug', populate_from='nome', always_update=True, unique=True)
    dono = models.ForeignKey(Usuario, verbose_name = 'Dono do Pacote', related_name = 'pacotes')
    codigo = models.CharField('Código do Pacote', max_length=5, unique=True)
    # codigo_pag_seguro = models.CharField('Código do Pag Seguro', max_length=32, unique=True)

    # itens = models.ManyToManyField(Item, verbose_name='Itens do pacote', related_name = 'itens')
    # seria um ManyToManyField com ItemPacote, mas sem o id do Pacote como está, apenas o item e a qtde (?)

    class Meta:
        verbose_name = 'Pacote'
        verbose_name_plural = 'Pacotes'

    def __str__(self):
        return str(self.nome)

    def as_json(self):
        return dict(
                id=self.id,
                slug=self.slug,
                nome=self.nome,
                quantidade_pessoas=self.quantidade_pessoas,
                preco=self.preco,
                dono=self.dono.id,
                codigo=self.codigo,
                itens=[i.item_as_json() for i in self.itens.all()]
            )

class Item(models.Model):
    nome = models.CharField('Nome do Item', max_length=200)
    preco = models.FloatField('Preço do Item')
    descricao = models.CharField('Descrição do Item', max_length=300, blank=True)
    criador = models.ForeignKey(Usuario, verbose_name = 'Criador do Item', related_name = 'itens')
    slug = AutoSlugField('Slug', populate_from='nome', always_update=True, unique=True)

    categorias = MultiSelectField(choices=MY_CHOICES, max_choices=3)

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'

    def __str__(self):
        return str(self.nome)

    def as_json(self):
        return dict(
                id=self.id,
                slug=self.slug,
                nome=self.nome,
                preco=self.preco,
                descricao=self.descricao,
                criador=self.criador.id,
                categorias=self.categorias
            )

class ItemPacote(models.Model):
    item = models.ForeignKey(Item, verbose_name='Item', related_name = 'itens_pacote')
    quantidade_item = models.PositiveIntegerField('Quantidade')
    pacote = models.ForeignKey(Pacote, verbose_name = 'Pacote do Item', related_name = 'itens')
    slug = AutoSlugField('Slug', populate_from='id', always_update=True, unique=True)

    class Meta:
        verbose_name = 'Quantidade-Item'
        verbose_name_plural = 'Quantidade-Itens'

    def __str__(self):
        return str(self.item) + " (" + str(self.quantidade_item) + ")"

    def item_as_json(self):
        return dict(
                id=self.item.id,
                slug=self.item.slug,
                nome=self.item.nome,
                preco=self.item.preco,
                descricao=self.item.descricao,
                quantidade=self.quantidade_item,
                categoria=self.item.categorias
            )
