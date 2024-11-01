from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from appHome.form_cadastro_usuario import FormCadastroUser
from appHome.form_cadastro_curso import FormCadastroCurso
from appHome.models import Usuario
from appHome.models import Curso
from appHome.form_login import FormLogin
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from datetime import timedelta

# Create your views here.


def home(request) :
    #recupera o email do usuario da sessao, se estiver presente
    email_do_usuario = request.session.get('email')

    context = {
        'email_do_usuario': email_do_usuario,
    }
    return render(request, "index.html", context)



def cadastrar_user(request):
    novo_user = FormCadastroUser(request.POST or None)

    if request.POST:
        email = request.POST.get('email')
        # Verificar se o e-mail já existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "E-mail já cadastrado.")
        elif novo_user.is_valid():
            user = novo_user.save(commit=False)
            # Criptografar a senha
            user.set_password(novo_user.cleaned_data['senha'])
            user.save()
            messages.success(request, "Usuário cadastrado com sucesso")
            return redirect('home')
    
    context = {'form': novo_user}
    return render(request, "cadastrar.html", context)


def cadastrar_curso(request):

    novo_curso = FormCadastroCurso(request.POST or None)

    if request.POST:
        if novo_curso.is_valid():
            novo_curso.save()
            messages.success(request, "Usuario cadastrado com sucesso")
            return redirect('home')
    context = {
        'form': novo_curso
    }
    return render(request, "cadastrar-curso.html", context)


def exibir_user(request):
    user = Usuario.objects.all().values()

    context = {
        'dados': user
    }

    return render(request, "user.html", context)


def exibir_curso(request):
    curso = Curso.objects.all().values()

    context = {
        'dados': curso
    }

    return render(request, "curso.html", context)



def fazer_login(request):
    formLogin = FormLogin(request.POST or None)
    if request.method == 'POST':
        if formLogin.is_valid():
            _email = formLogin.cleaned_data.get('email')
            _senha = formLogin.cleaned_data.get('senha')
            try:
                usuarioL = Usuario.objects.get(email = _email, senha = _senha)
                if usuarioL is not None:
                    #Define a duracao da sessao como 30 segunds
                    request.session.set_expiry(timedelta(seconds=30))
                    #cria uma sessao com o email do usuario
                    request.session['email'] = _email
                    return redirect('appHome')
            except Usuario.DoesNotExist:
                return render(request, 'login.html', {'error_message': 'Crenciais invalidas.'})
    
    context = {
        'form': formLogin
    }
    return render(request, 'form-login.html', context)
