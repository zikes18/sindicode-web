from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from associados.forms import AssociadoForm, LoginForm
from django.contrib import auth , messages



def associados(request):
    return render(request, 'associados/index.html')


def login(request):
    form = LoginForm(request.POST)
    #Verificar envio de requisição
    if request.method == 'POST':
        nome = form['nome_login'].value()
        senha = form['senha'].value()
        usuario = auth.authenticate(
            request,
            username=nome,
            password=senha
        )
        if usuario is not None:
            auth.login(request, usuario)
            messages.success(request, f'{nome}, BOA ZERO MEIA, fez o login')
            return redirect('beneficios')
        else:
            messages.error(request, 'Erro ao logar')
            return redirect('login')
    return render(request, 'associados/login.html', {'form': form})

def logout(request):
    #não esquecer request
    if request.user.is_authenticated:
        auth.logout(request)
        messages.success(request, 'Logout efetuado com sucesso')

    return redirect('login')

def cadastro(request):
    form = AssociadoForm()
    if request.method == 'POST':
        form = AssociadoForm(request.POST)
        if form.is_valid():
            if form['senha_1'].value() != form['senha_2'].value():
                messages.error(request, 'As senhas não são iguais')
                return redirect('cadastro')
            nome_completo = form['nome_completo'].value()
            nome_social = form['nome_social'].value()
            cpf = form['cpf'].value()
            rg = form['rg'].value()
            email = form['email'].value()
            identidade_genero = form['identidade_genero'].value()
            senha = form['senha_1'].value()
            if User.objects.filter(username=nome_completo).exists():
                messages.info(request, 'Nome de usuário já cadastrado')
                return redirect('cadastro')
            associado = User.objects.create_user(
                username = nome_completo,
                email = email,
                password = senha
            )
            associado.save()
            messages.success(request, f'{nome_completo}, Cadastrou com sucesso')
            return redirect('login')
    return render(request, 'associados/cadastro.html',{'form': form})
