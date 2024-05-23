from django.contrib import admin
from .models import Usuario, Item, Pedido

class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nome', 'email', 'cpf', 'celular')

class ItemAdmin(admin.ModelAdmin):
    list_display = ('nome', 'codigo_item', 'preco')

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'usuario', 'data_pedido')


admin.site.register(Usuario, UsuarioAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Pedido, PedidoAdmin)
