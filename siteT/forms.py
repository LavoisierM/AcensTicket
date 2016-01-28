from django import forms

from .models import Post
from .models import Usuario
from .models import Evento

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('author','title', 'text','created_date','published_date',)

class UsuarioForm(forms.ModelForm):

    class Meta:
	model = Usuario
	fields = ('name_user', 'email_user', 'senha',)

class EventoForm(forms.ModelForm):

	class Meta:
		model = Evento
		fields = ('titulo', 'data', 'descricao', 'responsavel',)
	
