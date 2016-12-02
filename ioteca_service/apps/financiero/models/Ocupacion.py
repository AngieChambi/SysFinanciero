from django.db import models


class Ocupacion(models.Model):

    nombre = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Ocupacion"
        verbose_name_plural = "Ocupaciones"

    def __str__(self):
        return self.nombre
