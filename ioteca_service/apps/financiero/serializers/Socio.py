from rest_framework import serializers
from ..models.Socio import Socio


class SocioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Socio
