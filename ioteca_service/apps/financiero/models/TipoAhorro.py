from django.db import models


class TipoAhorro(models.Model):

    nombre = models.CharField(max_length=30)

    class Meta:
        verbose_name = "TipoAhorro"
        verbose_name_plural = "TipoAhorros"

    def __str__(self):
        return self.nombre
