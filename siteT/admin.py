from django.contrib import admin
from .models import Post
from .models import Evento
from .models import Cliente
from .models import Usuario


admin.site.register(Post)
admin.site.register(Evento)
admin.site.register(Cliente)
admin.site.register(Usuario)

