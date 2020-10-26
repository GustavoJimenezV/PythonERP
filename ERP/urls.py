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
    path('Actividad/',views.Actividad),
    path('Asistencia/',views.Asistencia),
    path('Balance/',views.Balance),
    path('MenuCliente/',views.MenuCliente),
    path('MenuCliente/CrearCliente/',views.CrearCliente),
    path('Compra/',views.Compra),
    path('DetalleCompra/',views.DetalleCompra),
    path('Devoluciones/',views.Devoluciones),
    path('Empleado/',views.Empleado),
    path('Evaluacion/',views.Evaluacion),
    path('Jornada/',views.Jornada),
    path('Mantenimiento/',views.Mantenimiento),
    path('MateriaPrima/',views.MateriaPrima),
    path('Mobiliario/',views.Mobiliario),
    path('Pago/',views.Pago),
    path('Pedido/',views.Pedido),
    path('Permisos/',views.Permisos),
    path('Producto/',views.Producto),
    path('Proveedor/',views.Proveedor),
    path('Proyecto/',views.Proyecto),
    path('Remplazo/',views.Remplazo),
    path('Usuario/',views.Usuario),
    path('Venta/',views.Venta),
]
