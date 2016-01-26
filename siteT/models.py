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
    cod = models.CharField(max_length=2)
    titulo = models.CharField(max_length=10)
    data = models.DateTimeField(blank=True, null=True)
    descricao = models.TextField(max_length=200)
    responsavel = models.ForeignKey('auth.User')

class Cliente(models.Model):
    nome = models.CharField(max_length=20)
    dataNascimento = models.DateField(blank=True, null=True)
    CPF = models.CharField(max_length=8)
    endereco = models.CharField

class Usuario(models.Model):
    name_user = models.CharField(max_length=20)
    email_user = models.EmailField()
    senha = models.CharField(max_length=5)