from django.contrib import admin
from .models.Agencia import Agencia
from .models.Ahorro import Ahorro
from .models.Cargo import Cargo
from .models.Empleado import Empleado
from .models.Entrega import Entrega
from .models.Ocupacion import Ocupacion
from .models.Persona import Persona
from .models.Prestamo import Prestamo
from .models.ServFinanciero import ServFinanciero
from .models.Socio import Socio
from .models.TipoMovimiento import TipoMovimiento


admin.site.register(Agencia)
admin.site.register(Ahorro)
admin.site.register(Cargo)
admin.site.register(Empleado)
admin.site.register(Entrega)
admin.site.register(Ocupacion)
admin.site.register(Persona)
admin.site.register(Prestamo)
admin.site.register(ServFinanciero)
admin.site.register(Socio)
admin.site.register(TipoMovimiento)
