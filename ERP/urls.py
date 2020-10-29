"""ERP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Vistas import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.Login),
    path('Actividad/',views.MenuActividad),
    path('Asistencia/',views.MenuAsistencia),
    path('Balance/',views.MenuBalance),
    path('Cliente/',views.MenuCliente),
    path('GraficaCliente/',views.GraficaCliente),
    path('Compra/',views.MenuCompra),
    path('DetalleCompra/',views.MenuDetalleCompra),
    path('Devolucion/',views.MenuDevolucion),
    path('Empleado/',views.MenuEmpleado),
    path('Evaluacion/',views.MenuEvaluacion),
    path('Jornada/',views.MenuJornada),
    path('Mantenimiento/',views.MenuMantenimiento),
    path('MateriaPrima/',views.MenuMateriaPrima),
    path('Mobiliario/',views.MenuMobiliario),
    path('Pago/',views.MenuPago),
    path('Pedido/',views.MenuPedido),
    path('Permisos/',views.Permiso),
    path('Producto/',views.MenuProducto),
    path('Proveedor/',views.MenuProveedor),
    path('Proyecto/',views.MenuProyecto),
    path('Remplazo/',views.MenuRemplazo),
    path('Usuario/',views.CrearUsuario),
    path('Venta/',views.MenuVenta),
]
