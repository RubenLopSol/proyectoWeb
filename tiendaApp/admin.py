from django.contrib import admin
from .models import Categoria_producto, Producto

# Register your models here.

class Categoria_productoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields=('created', 'updated') 

admin.site.register(Categoria_producto, Categoria_productoAdmin)
admin.site.register(Producto, ProductoAdmin)