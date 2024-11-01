from django import forms
from appHome.models import Usuario

class FormLogin(forms.ModelForm):
    class Meta:  # Change 'meta' to 'Meta'
        model = Usuario
        fields = ('email', 'senha')

        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form_control border border-success', 'type':'email'}),  # Change to EmailInput
            'senha': forms.PasswordInput(attrs={'class': 'form_control border border-success', 'type':'password'})  # Ensure this is PasswordInput
        }

