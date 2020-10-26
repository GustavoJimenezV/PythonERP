from django.contrib import admin
from. models import Actividad, Asistencia, Balance, Empleado, Permisos
from. models import Cliente, Usuario
# Register your models here.
admin.site.register(Actividad)
admin.site.register(Asistencia)
admin.site.register(Balance)
admin.site.register(Empleado)
admin.site.register(Permisos)
admin.site.register(Usuario)




admin.site.register(Cliente)
