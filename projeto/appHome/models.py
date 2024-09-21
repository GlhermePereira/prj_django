from django.core.validators import EmailValidator
from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(validators=[EmailValidator()])
    senha = models.CharField(max_length=100)

