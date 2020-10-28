from django.contrib import admin
from. models import Actividad, Asistencia, Balance, Permiso
from. models import Cliente, Usuario,Proveedor,Empleado,Venta,Remplazo,Proyecto,Producto
# Register your models here.
#admin.site.register(Actividad)
#admin.site.register(Asistencia)
#admin.site.register(Balance)
admin.site.register(Empleado)
#admin.site.register(Permiso)
admin.site.register(Producto)
admin.site.register(Proveedor)
admin.site.register(Proyecto)
admin.site.register(Remplazo)
admin.site.register(Usuario)
admin.site.register(Venta)


admin.site.register(Cliente)
