from django.db import models
from .Persona import Persona
from .Cargo import Cargo
from .Agencia import Agencia


class Empleado(models.Model):

    persona = models.ForeignKey(Persona)
    codigo = models.CharField(max_length=4)
    cargo = models.ForeignKey(Cargo)
    iniciales = models.CharField(max_length=3)
    agencia = models.ForeignKey(Agencia)
    ventanilla = models.CharField(max_length=2)
    condicion = models.CharField(max_length=20)
    nivel = models.CharField(max_length=20)
    modificar_interes = models.BooleanField(default=False)  # por 15 min activo
    eliminar_movimiento = models.BooleanField(default=False)  # por 15 min
    modificar_socio = models.BooleanField(default=False)  # por 15 min
    rubro = models.CharField(max_length=30)

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"

    def __str__(self):
        return self.persona.nombres
