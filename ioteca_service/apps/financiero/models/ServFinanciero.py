from django.db import models


class ServFinanciero(models.Model):

    nombre = models.CharField(max_length=50)
    taza = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        verbose_name = "ServFinanciero"
        verbose_name_plural = "ServFinancieros"

    def __str__(self):
        return self.nombre
