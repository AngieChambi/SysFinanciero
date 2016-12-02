from rest_framework import viewsets
from ..models.TipoMovimiento import TipoMovimiento
from ..serializers.TipoMovimiento import TipoMovimientoSerializer


class TipoMovimientoViewSet(viewsets.ModelViewSet):
    queryset = TipoMovimiento.objects.all()
    serializer_class = TipoMovimientoSerializer
