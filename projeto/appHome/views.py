from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from appHome.form_cadastro_usuario import FormCadastroUser
from appHome.form_cadastro_curso import FormCadastroCurso
#from appHome.form_foto import FotoForm
from appHome.form_foto import FotoForm
from appHome.models import Usuario
from appHome.models import Curso
from appHome.form_login import FormLogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from appHome.form_resetar_senha import FormAlterarSenha
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

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

    if request.method == 'POST':
        email = request.POST.get('email')
        # Verificar se o e-mail já existe
        if Usuario.objects.filter(email=email).exists():
            messages.error(request, "E-mail já cadastrado.")
        elif novo_user.is_valid():
            user = novo_user.save(commit=False)
            # Criptografar a senha usando make_password
            user.senha = make_password(novo_user.cleaned_data['senha'])
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

def appHome(request):
    #Recupera a sessao do usuario se estiver ativa
    email_do_usuario = request.session.get('email')

    context = {
            'email_do_usuario': email_do_usuario,
            }
    return render(request, "index.html", context)

def dashboard(request):
    # Verificar se o usuário está autenticado
    if 'email' not in request.session:
        return redirect('fazer_login')

    # Obter a lista de usuários
    userList = Usuario.objects.all().values()  # Obtém todos os usuários como dicionários

    # Passar a lista de usuários para o contexto
    context = {
        'usuarios': userList,
        'email': request.session['email']  # Passa o email do usuário autenticado para exibir no template
    }

    # Carregar o template e renderizar com o contexto
    template = loader.get_template("dashboard.html")
    return HttpResponse(template.render(context))

def excluir_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id=id_usuario)
    usuario.delete()
    return redirect('home')

    return redirect('dashboard')
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
                usuarioL = Usuario.objects.get(email=_email)
                if usuarioL.check_password(_senha):  # Usar check_password
                    request.session.set_expiry(1800) 

                    request.session['email'] = _email
                    return redirect('dashboard')
                else:
                    return render(request, 'login.html', {'form': formLogin, 'error_message': 'Crédenciais inválidas.'})
            except Usuario.DoesNotExist:
                return render(request, 'login.html', {'form': formLogin, 'error_message': 'Crédenciais inválidas.'})

    context = {
        'form': formLogin
    }
    return render(request, 'registration/login.html', context)


def redefinir_senha(request, id_usuario):
    user = get_object_or_404(Usuario, id=id_usuario)  # Obtém o usuário pelo ID
    if request.method == 'POST':
        form = FormAlterarSenha(user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Mantém o usuário logado
            messages.success(request, 'Senha alterada com sucesso!')
            return redirect('dashboard')  # Redirecione para a página desejada
    else:
        form = FormAlterarSenha(user)

    return render(request, 'redefinir_senha.html', {'form': form, 'user': user})

def criar_foto(request):
    if request.method == 'POST':
        form = FotoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('pagina_sucesso')
    else:
        form = FotoForm()  # Esse formulário será exibido em uma requisição GET

    return render(request, 'criar_foto.html', {'form': form})

def pagina_sucesso(request):
    return render(request,'pagina_sucesso.html')
