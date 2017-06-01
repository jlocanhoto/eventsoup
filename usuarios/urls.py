from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'crud-fornecedor-buffet', views.FornecedorBuffetViewSet)
router.register(r'crud-contratante', views.ContratanteViewSet)

urlpatterns = [
    url(r'', include(router.urls)),
]
