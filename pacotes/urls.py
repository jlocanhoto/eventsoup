from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'crud-itens', views.ItemViewSet)
# router.register(r'crud-pacotes', views.PacoteViewSet)
# router.register(r'crud-item-pacote/(?P<slug_pacote>[^/.]+)', views.ItemPacoteViewSet)

urlpatterns = [
    url(r'list-all-pacotes/$', views.ListPacotes.as_view(),name = 'list-all-pacotes'),
    url(r'pacote-selecionado/(?P<slug>[^/.]+)', views.PacoteSelecionado.as_view(), name='pacote-selecionado'),
    url(r'my-pacotes/$', views.AllPacotes.as_view(), name='my-pacotes'),
    url(r'', include(router.urls)),
]
