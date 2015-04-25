# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tarefa',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('nome', models.CharField(verbose_name='nome', max_length=100)),
                ('descricao', models.TextField(verbose_name='descrição')),
                ('data_de_criacao', models.DateTimeField(verbose_name='data de criação', auto_now_add=True)),
                ('data_de_execucao', models.DateTimeField(verbose_name='date de execução')),
                ('finalizado', models.BooleanField(verbose_name='finalizado', default=False)),
            ],
            options={
                'verbose_name': 'tarefa',
                'ordering': ['-data_de_criacao'],
                'verbose_name_plural': 'tarefas',
            },
            bases=(models.Model,),
        ),
    ]
