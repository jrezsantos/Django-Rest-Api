from rest_framework import serializers
from .models import Usuario, Item, Pedido

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
    itens = ItemSerializer(many=True)
    class Meta:
        model = Pedido
        fields = '__all__'