from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
#Curso com os atributos nome, autor, duracao e preco, sendo o preco do tipo DecimalField(max_digits=10, decimal_places=2).
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, nome, senha=None, **extra_fields):
        if not email:
            raise ValueError('O usuário deve ter um endereço de email')
        email = self.normalize_email(email)
        user = self.model(email=email, nome=nome, **extra_fields)
        user.set_password(senha)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, nome, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser deve ter is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser deve ter is_superuser=True.')

        return self.create_user(email, nome, senha, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128, null=True)  # Defina como nulo ou com um valor padrão
    senha = models.CharField(max_length=128, null=True)  # Use um max_length adequado para a senha criptografada
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)    
    objects = UsuarioManager()


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    def __str__(self):
        return self.email

