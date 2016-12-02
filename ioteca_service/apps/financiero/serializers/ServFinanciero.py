from rest_framework import serializers
from ..models.ServFinanciero import ServFinanciero


class ServFinancieroSerializer(serializers.ModelSerializer):

    class Meta:
        model = ServFinanciero
