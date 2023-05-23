from django.shortcuts import render
from blogApp.models import Post, Categoria


# Create your views here.
def blog(request):

    posts=Post.objects.all()
    categoria=Categoria.objects.all()

    return render(request, "blogApp/blog.html", {"posts":posts, "categorias":categoria})

def categoria(request, categoria_id):

    categoria=Categoria.objects.get(id=categoria_id)
    posts=Post.objects.filter(categorias=categoria)

    return render(request, "blogApp/categoria.html", {"categoria":categoria, "posts":posts})