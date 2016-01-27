from django.shortcuts import render

# Create your views here.
def primeira(request):
	return render(request, 'siteT/primeira.html',{})
