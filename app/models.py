from django.db import models

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    widgets = {
        'nome': 'text',
        'telefone': 'text',
    }
    labels = {
        'nome': 'Nome',
        'telefone': 'Telefone',
    }
