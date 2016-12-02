from rest_framework import viewsets
from ..models.ServFinanciero import ServFinanciero
from ..serializers.ServFinanciero import ServFinancieroSerializer


class ServFinancieroViewSet(viewsets.ModelViewSet):
    queryset = ServFinanciero.objects.all()
    serializer_class = ServFinancieroSerializer
