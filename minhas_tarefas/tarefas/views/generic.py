from django.views.generic import ArchiveIndexView
from django.views.generic import DetailView
from tarefas.models import Tarefa
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class TarefasView(ArchiveIndexView):
    model = Tarefa
    date_field = 'data_de_criacao'

    @method_decorator(login_required)
    def get(self, request, *args, **kwargs):
        self.queryset = Tarefa.objects.filter(usuario=request.user.id)
        return super().get(request, *args, **kwargs)


class TarefasDetail(DetailView):
    model = Tarefa

__all__ = [
    'TarefasView',
    'TarefasDetail'
]
