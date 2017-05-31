from django.contrib import admin
from .models import Usuario
from .forms import UsuarioCreateForm, UsuarioChangeForm

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'cpf_cnpj', 'telefone']
    search_fields = ['nome', 'email', 'cpf_cnpj', 'telefone']

    def get_form(self, request, obj=None, **kwargs):
        if obj:
            self.form = UsuarioChangeForm
        else:
            self.form = UsuarioCreateForm
        return super(UsuarioAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(Usuario, UsuarioAdmin)
