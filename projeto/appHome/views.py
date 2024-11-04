from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from appHome.form_cadastro_usuario import FormCadastroUser
from appHome.form_cadastro_curso import FormCadastroCurso
from appHome.models import Usuario
from appHome.models import Curso
from appHome.form_login import FormLogin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.contrib.auth import update_session_auth_hash
from appHome.form_resetar_senha import PasswordResetForm
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


#redefinir senha

User = get_user_model()

@login_required
def redefinir_senha(request, id_usuario):
    # Busca o usuário pelo ID
    try:
        usuario = User.objects.get(id=id_usuario)
    except User.DoesNotExist:
        messages.error(request, 'Usuário não encontrado.')
        return redirect('dashboard')  # Redirecione para o dashboard ou outra página

    if request.method == "POST":
        form = PasswordResetForm(request.POST)

        if form.is_valid():
            senha_atual = form.cleaned_data['senha_atual']
            nova_senha = form.cleaned_data['nova_senha']
            confirmar_nova_senha = form.cleaned_data['confirmar_nova_senha']

            # Verifica se a senha atual está correta
            if not request.user.check_password(senha_atual):
                form.add_error('senha_atual', 'A senha atual está incorreta.')
            elif nova_senha != confirmar_nova_senha:
                form.add_error('confirmar_nova_senha', 'A nova senha e a confirmação não coincidem.')
            else:
                # Redefine a senha do usuário
                usuario.set_password(nova_senha)
                usuario.save()

                # Atualiza a sessão para evitar logout após a troca de senha
                update_session_auth_hash(request, usuario)
                messages.success(request, 'Sua senha foi alterada com sucesso.')
                return redirect('dashboard')  # Redirecione para o dashboard ou outra página
                
    else:
        form = PasswordResetForm()
    
    return render(request, 'redefinir_senha.html', {'form': form, 'usuario': usuario})

