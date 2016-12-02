from rest_framework import serializers
from ..models.Agencia import Agencia


class AgenciaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Agencia
