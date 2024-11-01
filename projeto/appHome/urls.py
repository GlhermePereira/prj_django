from django.urls import path

from . import views

urlpatterns = [
    path("home/", views.home, name="home"),
    path("cadastro/", views.cadastrar_user, name="cadastrar_user"),
    path("usuario/", views.exibir_user, name="exibir_user"),
    path("cadastroCurso/", views.cadastrar_curso, name="cadastro_curso"),
    path("curso/", views.exibir_curso, name="exibir_curso"),
    path("", views.fazer_login, name="fazer_login")
]
