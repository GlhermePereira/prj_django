import os
import django
import pytest
from django import forms
# Configuração do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projeto.settings')
django.setup()

# Importando os módulos após a configuração do Django
from appHome.form_cadastro import FormCadastroUser
from django.test import TestCase

class FormCadastroUserTest(TestCase):
    def test_form_fields(self):
        form = FormCadastroUser()
        # Teste se o widget do campo 'nome' é do tipo TextInput
        self.assertIsInstance(form.fields['nome'].widget, forms.TextInput)

