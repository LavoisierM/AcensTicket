from django.contrib.auth import authenticate, logout, login as authlogin
from django.shortcuts import render_to_response
from django.template import Context, loader, RequestContext
from django.shortcuts import render,  get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from siteT.models import Post
from .forms import UsuarioForm
from siteT.models import Evento
from .forms import EventoForm
from .models import Usuario

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

def login(request):

    if request.user.id:
        return render_to_response('siteT/login.html',(),context_instance=RequestContext(request, ()))


    if request.POST:
        name_user = request.POST.get('name_user')
        senha = request.POST.get('senha')
        u = authenticate(username=name_user,password=senha)
        if u is not None:
            if u.is_active:
                authlogin(request, u)

                if request.POST.get('next'):
                    return HttpResponseRedirect(request.POST.get('next'))
                
                return render_to_response('siteT/logado.html',(),context_instance=RequestContext(request, ()))

    return render_to_response('siteT/login.html',(),context_instance=RequestContext(request, ()))

def sair(request):
    logout(request)
    return render_to_response('siteT/login.html',(),context_instance=RequestContext(request, ()))

