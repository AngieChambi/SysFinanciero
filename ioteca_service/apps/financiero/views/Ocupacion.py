from rest_framework import viewsets
from ..models.Ocupacion import Ocupacion
from ..serializers.Ocupacion import OcupacionSerializer


class OcupacionViewSet(viewsets.ModelViewSet):
    queryset = Ocupacion.objects.all()
    serializer_class = OcupacionSerializer
