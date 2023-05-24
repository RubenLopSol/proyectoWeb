from django.shortcuts import render
from .models import Categoria_producto, Producto

# Create your views here.

def tienda(request):

    productos= Producto.objects.all()
    categorias= Categoria_producto.objects.all()

    return render(request, "tienda/tienda.html", {"productos":productos, "catecorias":categorias})

