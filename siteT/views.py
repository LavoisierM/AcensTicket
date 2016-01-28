from django.shortcuts import render,  get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

# Create your views here.
def primeira(request):
	return render(request, 'siteT/primeira.html',{})

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
