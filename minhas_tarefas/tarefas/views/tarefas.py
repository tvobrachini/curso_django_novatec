from django.shortcuts import redirect
from tarefas.forms import FormNovoUsuario
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


class CriaUsuario(View):
    template_name = 'tarefas/cria_usuario.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = FormNovoUsuario()
        return render_to_response(self.template_name, self.context,
                                  RequestContext(request))

    def post(self, request, *args, **kwargs):
        form = FormNovoUsuario(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
        else:
            self.context['form'] = form
            return render_to_response(self.template_name, self.context,
                                      RequestContext(request))

__all__ = [
    'Home',
    'CriaUsuario'
]
