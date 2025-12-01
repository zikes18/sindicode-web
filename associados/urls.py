from django.urls import path
from associados.views import associados, cadastro, login, login_view

urlpatterns = [
    path('associados',associados,name='associados'),
    path('login',login_view,name='login'),
    path('cadastro',cadastro,name='cadastro'),
]