from rest_framework import viewsets
from ..models.Socio import Socio
from ..serializers.Socio import SocioSerializer


class SocioViewSet(viewsets.ModelViewSet):
    queryset = Socio.objects.all()
    serializer_class = SocioSerializer
