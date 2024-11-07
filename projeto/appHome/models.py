from django.core.validators import EmailValidator
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin, Group, Permission
#Curso com os atributos nome, autor, duracao e preco, sendo o preco do tipo DecimalField(max_digits=10, decimal_places=2).
class Curso(models.Model):
    nome = models.CharField(max_length=100)
    autor = models.CharField(max_length=100)
    duracao = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

class UsuarioManager(BaseUserManager):
    def create_user(self, email, senha=None, **extra_fields):
        if not email:
            raise ValueError('O email deve ser fornecido.')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(senha)  # Usa set_password para armazenar a senha criptografada
        user.save(using=self._db)
        return user

    def create_superuser(self, email, senha=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        return self.create_user(email, senha, **extra_fields)


class Usuario(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    nome = models.CharField(max_length=30)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nome']

    groups = models.ManyToManyField(
        Group,
        related_name='usuario_set',  # Define um nome único para evitar conflito
        blank=True,
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name='usuario_set',  # Define um nome único para evitar conflito
        blank=True,
    )

    def __str__(self):
        return self.email

class Foto(models.Model):
    titulo = models.CharField(max_length=100)
    imagem = models.ImageField(upload_to='imagens/')


