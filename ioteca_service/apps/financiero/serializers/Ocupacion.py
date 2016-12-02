from rest_framework import serializers
from ..models.Ocupacion import Ocupacion


class OcupacionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Ocupacion
