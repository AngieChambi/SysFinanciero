from django.db import models


class TipoMovimiento(models.Model):

    nombre = models.CharField(max_length=70)
    taza = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "TipoMovimiento"
        verbose_name_plural = "TipoMovimientos"

    def __str__(self):
        return self.nombre
