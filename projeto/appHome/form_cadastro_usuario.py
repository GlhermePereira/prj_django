from django import forms  
from appHome.models import  Usuario

class FormCadastroUser(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form_control'}))

    class Meta:
        model = Usuario
        fields = ('nome', 'email')  # Remova 'senha' daqui
        widgets = {
            'nome': forms.TextInput(attrs={'class':'form_control'})
        }

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['senha'])  # Criptografa a senha
        if commit:
            user.save()
        return user
