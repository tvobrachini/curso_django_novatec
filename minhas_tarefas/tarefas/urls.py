from django.conf.urls import patterns, include, url
from tarefas.views import Home


urlpatterns = patterns(
    '',
    url(r'^$', Home.as_view()),
)