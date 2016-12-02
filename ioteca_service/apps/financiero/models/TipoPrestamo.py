from django.db import models


class TipoPrestamo(models.Model):

    nombre = models.CharField(max_length=70)
    taza = models.DecimalField(max_digits=6, decimal_places=2)

    class Meta:
        verbose_name = "TipoPrestamo"
        verbose_name_plural = "TipoPrestamos"

    def __str__(self):
        return self.nombre
