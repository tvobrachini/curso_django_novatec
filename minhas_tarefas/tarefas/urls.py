from django.conf.urls import patterns, include, url
from tarefas.views import Home
from tarefas.views import TarefasView
from tarefas.views import TarefasDetail
from tarefas.views import CriaUsuario


urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view(), name='home'),
    url(r'^tarefas/$', TarefasView.as_view(), name='tarefas'),
    url(r'^tarefas/(?P<pk>\d+)/$', TarefasDetail.as_view(),
        name='tarefas_detail'),
    url(r'^criar_usuario/$', CriaUsuario.as_view(), name='criar_usuario'),
)
