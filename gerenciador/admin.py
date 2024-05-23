from django.contrib import admin
from .models import Usuario, Item, Pedido, ListaPedidosUsuario

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'celular')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_item', 'preco')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data_pedido')

admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Pedido, PedidoAdmin)

class ListaPedidosUsuarioAdmin(admin.ModelAdmin):
    list_display = ['usuario', 'get_pedidos']

    def get_pedidos(self, obj):
        return ", ".join([str(pedido) for pedido in obj.pedidos.all()])
    get_pedidos.short_description = 'Pedidos'