from django.db import models
from .Persona import Persona
from .Ocupacion import Ocupacion


class Socio(models.Model):

    persona = models.ForeignKey(Persona)
    razon_social = models.CharField(max_length=50)
    domicilio = models.CharField(max_length=200)
    referencia = models.CharField(max_length=200)
    medidor = models.CharField(max_length=7)
    tipo_vivienda = models.CharField(max_length=40)
    observacion = models.CharField(max_length=200, blank=True, null=True)
    ocupacion = models.ForeignKey(Ocupacion)
    codigo = models.IntegerField()  # autoincremet
    fecha = models.DateField(auto_now_add=True)
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = "Socio"
        verbose_name_plural = "Socios"

    def __str__(self):
        return self.persona.nombres
