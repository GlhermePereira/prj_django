from django import forms
from appHome.models import Usuario
from django.core.exceptions import ValidationError

class FormLogin(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form_control', 'placeholder': 'Email'}))
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form_control', 'placeholder': 'Senha'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get("email")
        senha = cleaned_data.get("senha")

        try:
            user = Usuario.objects.get(email=email)  # Use objects.get() para buscar pelo e-mail
            if not user.check_password(senha):  # Usar check_password para verificar a senha
                raise ValidationError("Senha incorreta.")
        except Usuario.DoesNotExist:
            raise ValidationError("Usuário não encontrado.")

        return cleaned_data

