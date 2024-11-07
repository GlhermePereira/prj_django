from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm

class FormAlterarSenha(PasswordChangeForm):
    def __init__(self, user=None, *args, **kwargs):
        super(FormAlterarSenha, self).__init__(user, *args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Senha Atual'})
        self.fields['new_password1'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Nova Senha'})
        self.fields['new_password2'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Confirme Nova Senha'})

