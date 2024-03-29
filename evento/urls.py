from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'crud-eventos', views.EventoViewSet)
router.register(r'crud-endereco-evento/(?P<slug_evento>[^/.]+)', views.EnderecoViewSet)

urlpatterns = [
    url(r'proximos-eventos/$', views.ProximosEventos.as_view(),name = 'proximos-eventos'),
    # url(r'montar-evento/(?P<slug>[^/.]+)', views.EventoPacote.as_view(), name='montar-evento'),
    url(r'atualiza-status/(?P<slug>[^/.]+)', views.EventoAtualizaStatus.as_view(), name='montar-evento'),
    # url(r'remover-pacote-evento/(?P<slug>[^/.]+)', views.EventoRemoverPacote.as_view(), name='remover-pacote-evento'),
    url(r'pacotes-evento/(?P<slug>[^/.]+)', views.PacotesEvento.as_view(), name='pacotes-evento'),
    url(r'confirma-entrega-evento/', views.ConfirmaEntregaEvento.as_view(), name='confirma-entrega-evento'),
    url(r'', include(router.urls)),
]
