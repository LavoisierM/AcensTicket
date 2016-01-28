from django.shortcuts import render,  get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from siteT.models import Post
from .forms import UsuarioForm
from siteT.models import Evento
from .forms import EventoForm

# Create your views here.
def base(request):
	return render(request, 'siteT/base.html',{})

def post_detail (request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'siteT/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('siteT.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
        return render(request, 'siteT/post_edit.html', {'form': form})

def signup_user(request):
     if request.method == "POST":
         usuario = UsuarioForm(request.POST)
     	 if usuario.is_valid():
            usuario = usuario.save(commit=False)
            usuario.save()
            return redirect('siteT.views.signup_user')
     else:
      usuario = UsuarioForm()
      ctx = {'usuario': usuario}
      return render(request, 'siteT/signup_user.html', ctx)

def new_evento(request):
     if request.method == "POST":
         Evento = EventoForm(request.POST)
         if Evento.is_valid():
            Evento = Evento.save(commit=False)
            Evento.save()
            return redirect('siteT.views.new_evento')
     else:
      Evento = EventoForm()
      ctx = {'Evento': Evento}
      return render(request, 'siteT/new_evento.html', ctx)


