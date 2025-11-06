from django.db import models

# estudar ORM (object-relation-mapper)
class Categoria(models.Model):
    nome = models.CharField(max_length=80, null=False, blank=False)
    def __str__(self):
        return f"Categoria [nome={self.nome}]"

class Autor(models.Model):
    nome = models.CharField(max_length=80, null=False, blank=False)
    perfil = models.TextField(null=False, blank=False)
    def __str__(self):
        return self.nome+self.perfil
# Create your models here.
#python manage.py makemigrations
#python manage.py migrate