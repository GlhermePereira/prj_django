from django.db import models


# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=255)
    email = models.CharField(max_length=255, unique=True)
    senha = models.CharField(max_length=255)
