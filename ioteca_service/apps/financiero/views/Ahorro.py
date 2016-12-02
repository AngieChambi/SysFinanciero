from rest_framework import viewsets
from ..models.Ahorro import Ahorro
from ..serializers.Ahorro import AhorroSerializer


class AhorroViewSet(viewsets.ModelViewSet):
    queryset = Ahorro.objects.all()
    serializer_class = AhorroSerializer
