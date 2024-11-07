from django import forms
from appHome.models import Foto

class FotoForm(forms.ModelForm):
    class Meta:
        model = Foto
        fields = ['titulo', 'imagem']

        widgets = {
                'imagem': forms.FileInput(attrs={'accept': 'image/*'})
                }

