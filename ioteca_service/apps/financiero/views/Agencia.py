from rest_framework import viewsets
from ..models.Agencia import Agencia
from ..serializers import AgenciaSerializer


class AgenciaViewSet(viewsets.ModelViewSet):
    queryset = Agencia.objects.all()
    serializer_class = AgenciaSerializer
