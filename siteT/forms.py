from django import forms

from .models import Post
from .models import Usuario

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)

class UsuarioForm(forms.ModelForm):

    class Meta:
	model = Usuario
	fields = ('name_user', 'email_user', 'senha',)
	
