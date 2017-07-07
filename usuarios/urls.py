from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'crud-fornecedor-buffet', views.FornecedorBuffetViewSet)
router.register(r'crud-usuario-endereco', views.EnderecoViewSet)
router.register(r'crud-contratante', views.ContratanteViewSet)

urlpatterns = [
    url(r'^verifica-autenticacao/$', views.VerificarAutenticacao.as_view(), name="verifica-autenticacao"),
    url(r'', include(router.urls)),
]
