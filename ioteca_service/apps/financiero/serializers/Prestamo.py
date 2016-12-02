from rest_framework import serializers
from ..models.Prestamo import Prestamo


class PrestamoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prestamo
