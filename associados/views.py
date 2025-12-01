from django.shortcuts import render
from associados.forms import AssociadoForm

def associados(request):
    return render(request, 'associados/index.html')
def login(request):
    return render(request, 'associados/login.html')
def cadastro(request):
    form = AssociadoForm()
    return render(request, 'associados/cadastro.html',{'form': form})
def login_view(request):
    if request.method == 'POST':
        form = AssociadoForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('nome_completo')  # Supondo que seja 'nome_completo' como nome de usuário
            senha = form.cleaned_data.get('senha')
            user = authenticate(request, username=username, password=senha)
            if user is not None:
                login(request, user)
                return redirect('home')  # Ou qualquer página que você queira redirecionar após o login
            else:
                form.add_error(None, 'Usuário ou senha inválidos')
    else:
        form = AssociadoForm()

    return render(request, 'associados/login.html', {'form': form})