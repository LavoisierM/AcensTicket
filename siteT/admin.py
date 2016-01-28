from django.contrib import admin
from .models import Post
from .models import Evento
from .models import Cliente
from .models import Usuario
from django.contrib.admin.options import ModelAdmin

class UsuarioAdmin(ModelAdmin):
	list_display = ['name_user','email_user']

class ClienteAdmin(ModelAdmin):
	list_display = ['nome','data_nascimento', 'cpf', 'endereco']


admin.site.register(Post)
admin.site.register(Evento)
admin.site.register(Cliente)
admin.site.register(Usuario, UsuarioAdmin)

