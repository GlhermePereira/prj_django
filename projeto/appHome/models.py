from django.core.validators import EmailValidator
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    senha = models.CharField(max_length=100)
    
#Curso com os atributos nome, autor, duracao e preco, sendo o preco do tipo DecimalField(max_digits=10, decimal_places=2).
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
