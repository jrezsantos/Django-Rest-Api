from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from gerenciador.views import UsuarioViewSet, ItemViewSet, PedidoViewSet, ListaPedidosUsuarioView

router = DefaultRouter()

router.register('usuarios', UsuarioViewSet)
router.register('itens', ItemViewSet)
router.register('pedidos', PedidoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('lista-pedidos/<int:pk>/', ListaPedidosUsuarioView.as_view(), name='lista_pedidos_usuario'),
]
