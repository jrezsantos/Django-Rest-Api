from rest_framework import viewsets, generics
from .models import Usuario, Item, Pedido, ListaPedidosUsuario
from .serializers import UsuarioSerializer, ItemSerializer, PedidoSerializer, ListaPedidosUsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ItemViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ListaPedidosUsuarioView(generics.RetrieveAPIView):
    queryset = ListaPedidosUsuario.objects.all()
    serializer_class = ListaPedidosUsuarioSerializer
