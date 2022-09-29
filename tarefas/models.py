from email.policy import default
from random import choices
from unittest.mock import DEFAULT

from django.db import models
from django.forms import CharField


class Tarefas(models.Model):
    OPCOES_STATUS = (
        ('concluído', 'Concluído'),
        ('pendente', 'Pendente'),
        ('adiado', 'Adiado')
    )

    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito')
    )

    
    descricao = models.CharField(max_length=400)
    criacao = models.DateTimeField(auto_now_add=True)
    categoria = models.CharField(max_length=25, choices=OPCOES_CATEGORIA, default='importante')
    status = models.CharField(max_length=25, choices=OPCOES_STATUS, default='pendente')



    class Meta:
        verbose_name = 'Tarefa'
