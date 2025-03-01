from django import forms
from . import models

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = models.Usuario
        fields = ['nome', 'telefone']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'telefone': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome',
            'telefone': 'Telefone',
        }