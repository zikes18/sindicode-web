from django.urls import path
from beneficios.views import listar_beneficios

urlpatterns = [
    path('listar_beneficios',listar_beneficios,name='beneficios'),
]