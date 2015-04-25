from tarefas.models import Tarefa
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.forms import Form
from django.forms import CharField
from django.forms import EmailField
from django.forms import PasswordInput


class FormNovoUsuario(Form):
    nome_de_usuario = CharField()
    nome = CharField(required=False)
    email = EmailField(required=False)
    senha = CharField(widget=PasswordInput)
    repeticao_senha = CharField(widget=PasswordInput)

    def save(self):
        params = {
            'username': self.cleaned_data['nome_de_usuario'],
            'email': self.cleaned_data['email'],
            'password': self.cleaned_data['senha'],
        }
        if self.cleaned_data['nome']:
            params['first_name'] = self.cleaned_data['nome']
        User.objects.create_user(**params)

    def clean_repeticao_senha(self):
        senha1 = self.cleaned_data['senha']
        senha2 = self.cleaned_data['repeticao_senha']

        if senha1 != senha2:
            raise ValidationError('As Senhas devem ser iguais')
        return senha1


class FormTarefa(ModelForm):
    class Meta:
        model = Tarefa
        fields = ['nome', 'descricao', 'finalizado']
