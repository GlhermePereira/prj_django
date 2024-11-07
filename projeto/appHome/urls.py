from os import name
from django.urls import path, include
from django.conf import settings
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView
from django.conf.urls.static import static

urlpatterns = [
    path("home/", views.home, name="home"),
    path("cadastro/", views.cadastrar_user, name="cadastrar_user"),
    path("usuario/", views.exibir_user, name="exibir_user"),
    path("cadastroCurso/", views.cadastrar_curso, name="cadastro_curso"),
    path("curso/", views.exibir_curso, name="exibir_curso"),
    path("appHome/", views.appHome, name="appHome"),
    path("", views.fazer_login, name="fazer_login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path('excluir_usuario/<int:id_usuario>/', 
         views.excluir_usuario, name='excluir_usuario'),
    path("criaFoto/", views.criar_foto, name="criar_foto"),
    path('succes/', views.pagina_sucesso, name="pagina_sucesso"),
    path('redefinir_senha/<int:id_usuario>/', 
         views.redefinir_senha, name="redefinir_senha"),
    path('galeria/', views.mostrar_fotos, name="galeria"),
    #path('perfilUsuario/', views.perfil_usuario, name="perfil_usuario"),
           ] 

