# forms.py
from django import forms

class PasswordResetForm(forms.Form):
    senha_atual = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Senha Atual'}))
    nova_senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Nova Senha'}))
    confirmar_nova_senha = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirme a Nova Senha'}))
