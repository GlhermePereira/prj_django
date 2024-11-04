from os import name
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView

urlpatterns = [
    path("home/", views.home, name="home"),
    path("cadastro/", views.cadastrar_user, name="cadastrar_user"),
    path("usuario/", views.exibir_user, name="exibir_user"),
    path("cadastroCurso/", views.cadastrar_curso, name="cadastro_curso"),
    path("curso/", views.exibir_curso, name="exibir_curso"),
    path("appHome/", views.appHome, name="appHome"),
    path("", views.fazer_login, name="fazer_login"),
    #path("", LoginView.as_view(template_name='registration/login.html'), name="fazer_login"),
    path("dashboard", views.dashboard, name="dashboard"),
    path('excluir_usuario/<int:id_usuario>/', views.excluir_usuario, name='excluir_usuario'),
    path('redefinir_senha/<int:id_usuario>/', views.redefinir_senha, name='redefinir_senha'),
    #path('accounts/login/', auth_views.LoginView.as_view(), name='login'),  # URL para a página de login
]
