from rest_framework import viewsets
from ..models.Cargo import Cargo
from ..serializers.Cargo import CargoSerializer


class CargoViewSet(viewsets.ModelViewSet):
    queryset = Cargo.objects.all()
    serializer_class = CargoSerializer
