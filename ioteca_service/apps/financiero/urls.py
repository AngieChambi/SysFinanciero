from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from .views.Agencia import AgenciaViewSet
from .views.Ahorro import AhorroViewSet
from .views.Cargo import CargoViewSet
from .views.Empleado import EmpleadoViewSet
from .views.Entrega import EntregaViewSet
from .views.Ocupacion import OcupacionViewSet
from .views.Persona import PersonaViewSet
from .views.Prestamo import PrestamoViewSet
from .views.ServFinanciero import ServFinancieroViewSet
from .views.Socio import SocioViewSet
from .views.TipoMovimiento import TipoMovimientoViewSet

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'agencias', AgenciaViewSet)
router.register(r'ahorros', AhorroViewSet)
router.register(r'cargos', CargoViewSet)
router.register(r'empleados', EmpleadoViewSet)
router.register(r'entregas', EntregaViewSet)
router.register(r'ocupaciones', OcupacionViewSet)
router.register(r'personas', PersonaViewSet)
router.register(r'prestamos', PrestamoViewSet)
router.register(r'servfinancieros', ServFinancieroViewSet)
router.register(r'socios', SocioViewSet)
router.register(r'tipomovimientos', TipoMovimientoViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
]