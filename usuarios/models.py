from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
import unicodedata
from django.utils.encoding import force_text
from django.utils import timezone
from autoslug import AutoSlugField

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, cpf_cnpj, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        if not email:
            raise ValueError('O campo email é obrigatorio')

        if not cpf_cnpj:
            raise ValueError('O campo CPF/CNPJ é obrigatorio')

        email = self.normalize_email(email)
        cpf_cnpj = self.model.normalize_cpf_cnpj(cpf_cnpj)
        user = self.model(cpf_cnpj=cpf_cnpj, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, cpf_cnpj, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(cpf_cnpj, email, password, **extra_fields)

    def create_superuser(self, cpf_cnpj, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(cpf_cnpj, email, password, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField('Nome', max_length = 100)
    email = models.EmailField('Email', unique = True)
    telefone = models.CharField('Telefone', max_length = 30)
    cpf_cnpj = models.CharField('CPF/CNPJ', max_length = 30, unique = True)
    endereco = models.CharField('Endereço', max_length = 200)
    is_staff = models.BooleanField('Staff Status',default=False)
    is_active = models.BooleanField('Ativo', default=True)
    date_joined = models.DateTimeField('Data de Cadastro', default=timezone.now)
    slug = AutoSlugField('Slug', populate_from='nome', unique_with=('date_joined'), unique=True)

    USERNAME_FIELD = 'cpf_cnpj'
    REQUIRED_FIELDS = ['email']

    objects = UserManager()

    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'

    def __str__(self):
        return str(self.nome) or str(self.cpf_cnpj) or str(self.email)

    def get_short_name(self):
        return str(self)

    @classmethod
    def normalize_cpf_cnpj(cls, cpf_cnpj):
        return unicodedata.normalize('NFKC', force_text(cpf_cnpj))

class Contratante(Usuario):

    class Meta:
        verbose_name = 'Contratante'
        verbose_name_plural = 'Contratantes'

class FornecedorBuffer(Usuario):

    faz_entrega = models.BooleanField('Faz entrega')

    class Meta:
        verbose_name = 'Fornecedor (Buffer)'
        verbose_name_plural = 'Fornecedores (Buffer)'

class Entregador(Usuario):

    VEICULOS = (('Moto', 'Moto'),
                ('Carro', 'Carro'),
                ('Van', 'Van'),
                ('Caminhao', 'Caminhão'))

    veiculo = models.CharField('Veiculo', max_length = 50, choices = VEICULOS)

    class Meta:
        verbose_name = 'Entregador'
        verbose_name_plural = 'Entregadores'
