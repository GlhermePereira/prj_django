from django import forms  
from appHome.models import  Usuario

class FormCadastroUser(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('nome','email','senha')
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form_control'})
        }
