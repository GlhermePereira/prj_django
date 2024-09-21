from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from appHome.form_cadastro import FormCadastroUser
from appHome.models import Usuario
# Create your views here.

def home(request):
    template = loader.get_template("index.html")
    return HttpResponse(template.render())


def cadastrar_user(request):

    novo_user = FormCadastroUser(request.POST or None)
    #salver usuario
    if request.POST:
        if novo_user.is_valid():
            novo_user.save()
            messages.success(request,"Usuario cadastrado com sucesso")
            return redirect('home')
    context = {
        'form': novo_user
    }
    return render(request, "cadastrar.html",context)

def exibir_user(request):
    user = Usuario.objects.all().values()

    context = {
        'dados': user
    }

    return render(request, "user.html", context)
