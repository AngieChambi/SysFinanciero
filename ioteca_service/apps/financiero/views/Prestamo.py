from rest_framework import viewsets
from ..models.Prestamo import Prestamo
from ..serializers.Prestamo import PrestamoSerializer


class PrestamoViewSet(viewsets.ModelViewSet):
    queryset = Prestamo.objects.all()
    serializer_class = PrestamoSerializer
