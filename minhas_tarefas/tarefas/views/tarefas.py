from django.views.generic import View
from django.shortcuts import render_to_response
from django.template.context import RequestContext
from tarefas.models import Tarefa


class Home(View):
    template_name = 'tarefas/home.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['counter'] = Tarefa.objects.filter(
            finalizado=False).count()
        return render_to_response(self.template_name, self.context,
                                  RequestContext(request))

__all__ = [
    'Home'
]
