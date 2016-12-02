from rest_framework import serializers
from ..models.Cargo import Cargo


class CargoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cargo
