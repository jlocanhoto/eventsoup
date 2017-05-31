from django.conf.urls import url, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'crud-eventos', views.EventoViewSet)

urlpatterns = [
    url(r'list-owner-eventos/$', views.ListOwnerEventos.as_view(),name = 'list-owner-eventos'),
    url(r'', include(router.urls)),
]
