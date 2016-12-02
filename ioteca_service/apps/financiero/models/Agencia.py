from django.db import models


class Agencia(models.Model):

    nombre = models.CharField(max_length=20)
    codigo = models.CharField(max_length=2)
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Agencia"
        verbose_name_plural = "Agencias"

    def __str__(self):
        return self.nombre
