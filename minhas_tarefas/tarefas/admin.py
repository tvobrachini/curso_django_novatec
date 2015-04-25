from django.contrib.admin import site
from django.contrib.admin import ModelAdmin
from tarefas.models import Tarefa


class TarefaAdmin(ModelAdmin):
    list_display = ['nome', 'descricao', 'data_de_criacao', 'finalizado']
    fields = ['nome', 'descricao', 'finalizado']
    # exclude = ['data_de_criacao']
    list_editable = ['finalizado']
    search_fields = ['nome']

site.register(Tarefa, TarefaAdmin)
