from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
# Create your views here.
def Actividad(request):
    DocExterno = loader.get_template("Actividad.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Asistencia(request):
    DocExterno = loader.get_template("Asistencia.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Balance(request):
    DocExterno = loader.get_template("Balance.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Cliente(request):
    DocExterno = loader.get_template("Cliente.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Compra(request):
    DocExterno = loader.get_template("Compra.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def DetalleCompra(request):
    DocExterno = loader.get_template("DetalleCompra.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Devoluciones(request):
    DocExterno = loader.get_template("Devoluciones.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Empleado(request):
    DocExterno = loader.get_template("Empleado.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Evaluacion(request):
    DocExterno = loader.get_template("Evaluacion.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Jornada(request):
    DocExterno = loader.get_template("Jornada.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Mantenimiento(request):
    DocExterno = loader.get_template("Mantenimiento.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def MateriaPrima(request):
    DocExterno = loader.get_template("MateriaPrima.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Mobiliario(request):
    DocExterno = loader.get_template("Mobiliario.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Pago(request):
    DocExterno = loader.get_template("Pago.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Pedido(request):
    DocExterno = loader.get_template("Pedido.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Permisos(request):
    DocExterno = loader.get_template("Permisos.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Producto(request):
    DocExterno = loader.get_template("Producto.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Proveedor(request):
    DocExterno = loader.get_template("Proveedor.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Proyecto(request):
    DocExterno = loader.get_template("Proyecto.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Remplazo(request):
    DocExterno = loader.get_template("Remplazo.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Usuario(request):
    DocExterno = loader.get_template("Usuario.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Venta(request):
    DocExterno = loader.get_template("Venta.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)
