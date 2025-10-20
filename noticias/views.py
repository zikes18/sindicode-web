from django.shortcuts import render
from django.http import HttpResponse

# função
# se def dentro classe = metodo
# se def fora classe = funçao
def index(request):
    #return HttpResponse("<h1>Alô Django 2005</h1>")
    return render(request, 'noticias/index.html')
