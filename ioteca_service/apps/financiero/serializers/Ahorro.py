from rest_framework import serializers
from ..models.Ahorro import Ahorro


class AhorroSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ahorro
