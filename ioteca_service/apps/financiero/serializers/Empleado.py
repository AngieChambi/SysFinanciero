from rest_framework import serializers
from ..models.Empleado import Empleado


class EmpleadoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Empleado
