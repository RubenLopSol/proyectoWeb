from django.contrib import admin
from .models import Pedido, Linea_Pedido

# Register your models here.

# class PedidoAdmin(admin.ModelAdmin):
#     pass

# class Linea_PedidoAdmin(admin.ModelAdmin):
#     pass

# admin.site.register(Pedido, PedidoAdmin)
# admin.site.register(Linea_Pedido, Linea_PedidoAdmin)

admin.site.register([Pedido, Linea_Pedido])