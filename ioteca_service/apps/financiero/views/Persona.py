from rest_framework import viewsets
from ..models.Persona import Persona
from ..serializers.Persona import PersonaSerializer


class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer
