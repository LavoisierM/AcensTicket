from django.db import models
from django.utils import timezone
from django import forms

class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Evento(models.Model):
    listaEvento = list(range(100))
    cod = models.CharField(max_length=2)
    titulo = models.CharField(max_length=10)
    data = models.DateTimeField(blank=True, null=True)
    descricao = models.TextField(max_length=200)
    responsavel = models.ForeignKey('auth.User')

class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    data_nascimento = models.DateField(blank=True, null=True)
    cpf = models.CharField(max_length=11, default = 'blank')
    endereco = models.CharField

    def __unicode__(self):
        return self.nome

class Usuario(models.Model):
    name_user = models.CharField(max_length=20)
    email_user = models.EmailField()
    senha = models.CharField(max_length=5)

    def __unicode__(self):
        return self.name_user

#    def compraIngresso(self):
#	nome = raw_input("Digite o nome do evento")
#	for Evento.nome in listaEvento:
#		opcao = input("Deseja comprar ingresso?1 para sim e 2 para nao")
#		if (opcao == 1):
#			return true
#		if (opcao == 2):
#			return false

