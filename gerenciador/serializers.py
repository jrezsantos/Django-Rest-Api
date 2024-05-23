from rest_framework import serializers
from .models import Usuario, Item, Pedido, ListaPedidosUsuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class PedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pedido
        fields = '__all__'

class ListaPedidosUsuarioSerializer(serializers.ModelSerializer):
    usuario = serializers.ReadOnlyField(source='usuario.username')
    pedidos = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = ListaPedidosUsuario
        fields = ['usuario', 'pedidos']