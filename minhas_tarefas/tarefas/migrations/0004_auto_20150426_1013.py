# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0003_tarefa_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='usuario',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, related_name='tarefas', verbose_name='usuário', null=True),
            preserve_default=True,
        ),
    ]
