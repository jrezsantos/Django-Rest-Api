from rest_framework import viewsets, generics
from .models import Usuario, Item, Pedido
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

class ListaPedidosUsuario(generics.ListAPIView):
    def get_queryset(self):
        queryset = Pedido.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPedidosUsuarioSerializer
