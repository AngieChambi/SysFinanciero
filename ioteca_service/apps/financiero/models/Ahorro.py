from django.db import models
from .Socio import Socio
from .Empleado import Empleado
from .TipoMovimiento import TipoMovimiento
from .ServFinanciero import ServFinanciero


class Ahorro(models.Model):

    socio = models.ForeignKey(Socio)
    empleado = models.ForeignKey(Empleado)
    tipo_ahorro = models.ForeignKey(TipoMovimiento)
    serv_financiero = models.ForeignKey(ServFinanciero)
    importe = models.IntegerField()
    observacion = models.CharField(max_length=150, blank=True, null=True)

    class Meta:
        verbose_name = "Ahorro"
        verbose_name_plural = "Ahorros"

    def __str__(self):
        return "%s %s" % (self.socio.persona.nombres, self.importe)
