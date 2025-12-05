from django.shortcuts import render

def listar_beneficios(request):
    return render(request, "beneficios/listar_beneficios.html")
# Create your views here.
