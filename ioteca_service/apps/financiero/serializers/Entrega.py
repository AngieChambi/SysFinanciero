from rest_framework import serializers
from ..models.Entrega import Entrega


class EntregaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Entrega
