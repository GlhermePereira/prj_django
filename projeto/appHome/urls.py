from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("cadastro/",views.cadastrar_user, name="cadastrar_user"),
    path("usuario/",views.exibir_user, name="exibir_user"),
]
