from django.contrib import admin

from noticias.models import Categoria, Autor

admin.site.register(Categoria)
admin.site.register(Autor)
# Register your models here.