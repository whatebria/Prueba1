from django.shortcuts import render
from .models import Post


# Create your views here.
def home(request):
    title = "Inicio"

    data = {
        "title": title
    }

    return render(request, "app1/index.html", data)

def blog(request):
    title = "Blog"

    context = {
        'posts': Post.objects.all(),
        'title': title
    }
    return render(request, "app1/blog.html", context)

