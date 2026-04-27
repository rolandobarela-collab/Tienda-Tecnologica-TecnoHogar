from django.contrib import admin
from .models import Producto, Pedido, ItemPedido

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'stock', 'categoria', 'disponible']
    list_filter = ['categoria', 'disponible']
    search_fields = ['nombre']

@admin.register(Pedido)
class PedidoAdmin(admin.ModelAdmin):
    list_display = ['id', 'usuario', 'fecha', 'estado', 'total']
    list_filter = ['estado']

@admin.register(ItemPedido)
class ItemPedidoAdmin(admin.ModelAdmin):
    list_display = ['pedido', 'producto', 'cantidad', 'precio_unitario']