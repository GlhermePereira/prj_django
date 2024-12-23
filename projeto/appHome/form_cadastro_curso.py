from django import forms  
from appHome.models import Curso


class FormCadastroCurso(forms.ModelForm):
    class Meta:
        model = Curso
        fields = {'nome', 'autor','duracao', 'preco', 'imagem'}
        widgets = {
            'preco': forms.NumberInput(attrs={'step':'0.01'}),
            'imagem': forms.FileInput(attrs={'accept': 'image/*'}) 
            }
