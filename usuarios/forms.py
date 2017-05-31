from django.forms import ModelForm
from .models import Usuario
from django.contrib.auth import forms

class UsuarioCreateForm(forms.UserCreationForm):

    def clean_pk(self):
        pk = self.cleaned_data["pk"]
        try:
            Usuario.objects.get(pk=pk)
        except Usuario.DoesNotExist:
            return pk
        raise forms.ValidationError('pk já cadastrado')

    class Meta:
        model = Usuario
        fields = ['nome','cpf_cnpj','email','telefone']

class UsuarioChangeForm(ModelForm):

    class Meta:
        model = Usuario
        fields = ['nome','cpf_cnpj','email','telefone']
