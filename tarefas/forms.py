from django import forms

from .models import Tarefas


class AdicionarTarefa(forms.ModelForm):
    class Meta:
        model = Tarefas
        fields = ('descricao', 'categoria')


class EditarTarefaForm(forms.Form):
    OPCOES_CATEGORIA = (
        ('urgente', 'Urgente'),
        ('importante', 'Importante'),
        ('precisa ser feito', 'Precisa ser feito')
    )
    tarefa = forms.CharField(max_length=400)
    categoria = forms.ChoiceField(choices=OPCOES_CATEGORIA)
