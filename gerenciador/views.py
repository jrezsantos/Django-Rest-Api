from rest_framework import viewsets, generics
from .models import Usuario, Item, Pedido
from .serializers import UsuarioSerializer, ItemSerializer, PedidoSerializer, ListaPedidosUsuarioSerializer
from rest_framework.permissions import IsAuthenticated

class UsuarioViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class ItemViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

class PedidoViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class ListaPedidosUsuario(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        queryset = Pedido.objects.filter(usuario_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaPedidosUsuarioSerializer
