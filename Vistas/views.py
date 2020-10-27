from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from Vistas.models import Usuario,Cliente,Empleado,Proveedor
# Create your views here.
def Login(request):
    if request.GET :
        Nombre=request.GET["Nombre"]
        Password = request.GET["Password"]
        Tipo=request.GET["Tipo"]
        objeto = Usuario.objects.filter(Nombre=Nombre,Tipo=Tipo,Password=Password)
        if objeto:
            return render(request,"Home.html")
        else:
            return render(request,"Login.html",{"error":"si"})
    else:
        return render(request,"Login.html")


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

def MenuCliente(request):
    if request.POST:
        objeto = Cliente()
        objeto.Nombre = request.POST["Nombre"]
        objeto.ApellidoM = request.POST["ApellidoP"]
        objeto.ApellidoP = request.POST["ApellidoM"]
        objeto.Direccion = request.POST["Direccion"]
        objeto.Telefono = request.POST["Telefono"]
        objeto.Correo = request.POST["Correo"]
        objeto.Sexo = request.POST["Sexo"]
        objeto.FechaNacimiento = request.POST["FechaNacimiento"]
        objeto.save()
        clientes = Cliente.objects.all()
        return render(request,"Cliente.html",{"agregado":"si","clientes":clientes})
    else:
        clientes = Cliente.objects.all()
        return render(request,"Cliente.html",{"clientes":clientes})


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

def MenuEmpleado(request):
    if request.POST:
        objeto = Empleado()
        objeto.Nombre = request.POST["Nombre"]
        objeto.ApellidoP = request.POST["ApellidoP"]
        objeto.ApellidoM = request.POST["ApellidoM"]
        objeto.Correo = request.POST["Correo"]
        objeto.Rfc = request.POST["Rfc"]
        objeto.Telefono = request.POST["Telefono"]
        objeto.Sexo = request.POST["Sexo"]
        objeto.FechaIngreso = request.POST["FechaIngreso"]
        objeto.Cargo = request.POST["Cargo"]
        objeto.Salario = request.POST["Salario"]
        objeto.EstadoCivil = request.POST["EstadoCivil"]
        objeto.Nss = request.POST["Nss"]
        objeto.save()
        empleados = Empleado.objects.all()
        return render(request,"Empleado.html",{"agregado":"si","empleados":empleados})
    else:
        empleados = Empleado.objects.all()
        return render(request,"Empleado.html",{"empleados":empleados})

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

def Permiso(request):
    DocExterno = loader.get_template("Permiso.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Producto(request):
    DocExterno = loader.get_template("Producto.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def MenuProveedor(request):
    if request.POST:
        objeto = Proveedor()
        objeto.Nombre = request.POST["Nombre"]
        objeto.Telefono = request.POST["Telefono"]
        objeto.Direccion = request.POST["Direccion"]
        objeto.Correo = request.POST["Correo"]
        objeto.Rfc = request.POST["Rfc"]
        objeto.save()
        proveedores = Proveedor.objects.all()
        return render(request,"Proveedor.html",{"agregado":"si","proveedores":proveedores})
    else:
        proveedores = Proveedor.objects.all()
        return render(request,"Proveedor.html",{"proveedores":proveedores})

def Proyecto(request):
    DocExterno = loader.get_template("Proyecto.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def Remplazo(request):
    DocExterno = loader.get_template("Remplazo.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)

def CrearUsuario(request):
    if request.POST:
        objeto = Usuario()
        objeto.Nombre = request.POST["Nombre"]
        objeto.Password = request.POST["Password"]
        objeto.Tipo = request.POST["Tipo"]
        objeto.save()
        return render(request,"Login.html",{"agregado":"si"})
    else:
        return render(request,"Usuario.html")

def Venta(request):
    DocExterno = loader.get_template("Venta.html")
    Documento = DocExterno.render()
    return HttpResponse(Documento)
