from django.db.models import Model
from django.db.models import BooleanField
from django.db.models import CharField
from django.db.models import DateTimeField
from django.db.models import TextField


# Create your models here.
class Tarefa(Model):
    nome = CharField(max_length=100, verbose_name='nome')
    descricao = TextField(verbose_name='descrição')
    data_de_criacao = DateTimeField(auto_now_add=True,
                                    verbose_name='data de criação')
    data_de_execucao = DateTimeField(verbose_name='date de execução')
    finalizado = BooleanField(default=False, verbose_name='finalizado')

    class Meta:
        ordering = ['-data_de_criacao']
        verbose_name = 'tarefa'
        verbose_name_plural = 'tarefas'
