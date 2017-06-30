from django.conf.urls import url
from rest_framework import routers
from . import views

router = routers.DefaultRouter()

urlpatterns = [
    url(r'^comprar/$', views.comprar, name = "comprar"),
    url(r'^notificacao/$', views.notificacao, name = "index"),
]
