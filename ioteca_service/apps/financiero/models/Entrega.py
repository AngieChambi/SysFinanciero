from django.db import models
from .Prestamo import Prestamo


class Entrega(models.Model):

    prestamo = models.ForeignKey(Prestamo)
    fecha = models.DateField(auto_now_add=True)
    fec_primera_cuota = models.DateTimeField()

    class Meta:
        verbose_name = "Entrega"
        verbose_name_plural = "Entregas"

    def __str__(self):
        return self.prestamo.socio.persona.nombres
