from rest_framework import viewsets
from ..models.Entrega import Entrega
from ..serializers.Entrega import EntregaSerializer


class EntregaViewSet(viewsets.ModelViewSet):
    queryset = Entrega.objects.all()
    serializer_class = EntregaSerializer
