from django.db import models

class Persona(models.Model):

    nombres = models.CharField(max_length=30)
    ap_paterno = models.CharField(max_length=30)
    ap_materno = models.CharField(max_length=30)
    dni = models.CharField(max_length=8)
    celular = models.CharField(max_length=12)
    estado_civil = models.CharField(max_length=20)
    sexo = models.CharField(max_length=1)
    email = models.EmailField(max_length=50)
    fec_nacimiento = models.DateField()

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"

    def __str__(self):
        return self.nombres
