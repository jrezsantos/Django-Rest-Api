from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers, permissions
from gerenciador.views import UsuarioViewSet, ItemViewSet, PedidoViewSet, ListaPedidosUsuario
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Gerenciador API DRF",
        default_version='v1',
        description="API RESTful que gerencie usuários, pedidos e itens.",
        terms_of_service="#",
        contact=openapi.Contact(email="juarezpsatosf@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


router = routers.DefaultRouter()

router.register('usuarios', UsuarioViewSet, basename='Usuários')
router.register('itens', ItemViewSet, basename='Itens')
router.register('pedidos', PedidoViewSet, basename='Pedidos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls) ),
    path('usuarios/<int:pk>/pedidos/', ListaPedidosUsuario.as_view()),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
