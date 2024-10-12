from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from appHome.form_cadastro_usuario import FormCadastroUser
from appHome.form_cadastro_curso import FormCadastroCurso
from appHome.models import Usuario
from appHome.models import Curso
from appHome.form_login import FormLogin
# Create your views here.


def home(request) :
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def cadastrar_user(request):

    novo_user = FormCadastroUser(request.POST or None)
    '''Salvar user'''
    if request.POST:
        if novo_user.is_valid():
            novo_user.save()
            messages.success(request , "Usuario cadastrado com sucesso")
            return redirect('home')
    context = {
        'form': novo_user
    }
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


def form_login(request):
    formLogin = FormLogin(request.POST or None)

    if request.POST:
        _email = request.POST['email']
        _senha = request.POST['senha']

        usuario = Usuario.objects.get(email=_email, senha=_senha)

        if usuario is not None:
            messages.success(request, 'Usuario Encontrado!')
            return redirect('index')
        else:
            messages.error(request, 'Usuario Nao encontrado!')
            return redirect('form_login')

    context = {
        'form': formLogin
    }

    return render(request, 'form-login.html', context)
