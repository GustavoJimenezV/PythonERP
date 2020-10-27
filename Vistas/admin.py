from django.contrib import admin
from. models import Actividad, Asistencia, Balance, Permiso
from. models import Cliente, Usuario,Proveedor,Empleado
# Register your models here.
#admin.site.register(Actividad)
#admin.site.register(Asistencia)
#admin.site.register(Balance)
admin.site.register(Empleado)
#admin.site.register(Permiso)
admin.site.register(Proveedor)
admin.site.register(Usuario)




admin.site.register(Cliente)
