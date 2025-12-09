from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

def listar_beneficios(request):
    if not request.user.is_authenticated:
        messages.error(request, 'Usuário não logado')
        return redirect('login')
    return render(request, "beneficios/listar_beneficios.html")
# Create your views here.
