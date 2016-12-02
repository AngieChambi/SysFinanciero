from django.db import models
from .Socio import Socio
from .TipoMovimiento import TipoMovimiento


class Prestamo(models.Model):

    numero = models.CharField(max_length=5)
    fecha = models.DateField()
    socio = models.ForeignKey(Socio)
    tipo_prestamo = models.ForeignKey(TipoMovimiento)
    importe = models.IntegerField()
    cuotas = models.IntegerField()
    tiene_garante = models.BooleanField(default=False)
    tiene_pagare = models.BooleanField(default=False)
    firma_mutua = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Prestamo"
        verbose_name_plural = "Prestamos"

    def __str__(self):
        return "%s %s" % (self.numero, self.socio.persona.nombres)
