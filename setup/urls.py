from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from gerenciador.views import UsuarioViewSet, ItemViewSet, PedidoViewSet, ListaPedidosUsuario

router = routers.DefaultRouter()

router.register('usuarios', UsuarioViewSet, basename='Usuários')
router.register('itens', ItemViewSet, basename='Itens')
router.register('pedidos', PedidoViewSet, basename='Pedidos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('usuario/<int:pk>/pedidos/', ListaPedidosUsuario.as_view())
]
