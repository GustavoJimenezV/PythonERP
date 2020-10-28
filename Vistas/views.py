from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from Vistas.models import Usuario,Cliente,Empleado,Proveedor,Venta,Remplazo,Proyecto,Producto
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

def MenuProducto(request):
    if request.POST:
        objeto = Producto()
        objeto.Nombre = request.POST["Nombre"]
        objeto.Descripcion = request.POST["Descripcion"]
        objeto.PrecioV = request.POST["PrecioVenta"]
        objeto.PrecioC = request.POST["PrecioCompra"]
        objeto.CantMin = request.POST["CantidadMin"]
        objeto.CantMax = request.POST["CantidadMax"]
        objeto.Categoria = request.POST["Categoria"]
        objeto.save()
        productos = Producto.objects.all()
        return render(request,"Producto.html",{"agregado":"si","productos":productos})
    else:
        productos = Producto.objects.all()
        return render(request,"Producto.html",{"productos":productos})


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

def MenuProyecto(request):
    if request.POST:
        objeto = Proyecto()
        objeto.NombrePro = request.POST["NombrePro"]
        objeto.TipoPro = request.POST["TipoProyecto"]
        objeto.IdEmpleado = request.POST["IdEmpleado"]
        objeto.FechaIn = request.POST["FechaInicio"]
        objeto.FechaFin = request.POST["FechaFinal"]
        objeto.Descripcion = request.POST["Descripcion"]
        objeto.save()
        proyectos = Proyecto.objects.all()
        return render(request,"Proyecto.html",{"agregado":"si","proyectos":proyectos})
    else:
        proyectos = Proyecto.objects.all()
        return render(request,"Proyecto.html",{"proyectos":proyectos})

def MenuRemplazo(request):
    if request.POST:
        objeto = Remplazo()
        objeto.IdMobiliario = request.POST["IdMobiliario"]
        objeto.Fecha = request.POST["Fecha"]
        objeto.Costo = request.POST["Costo"]
        objeto.Descripcion = request.POST["Descripcion"]
        objeto.save()
        remplazos = Remplazo.objects.all()
        return render(request,"Remplazo.html",{"agregado":"si","remplazos":remplazos})
    else:
        remplazos = Remplazo.objects.all()
        return render(request,"Remplazo.html",{"remplazos":remplazos})

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

def MenuVenta(request):
    if request.POST:
        objeto = Venta()
        objeto.Fecha = request.POST["Fecha"]
        objeto.IdCliente = request.POST["IdCliente"]
        objeto.Total = request.POST["Total"]
        objeto.TipoPago = request.POST["TipoPago"]
        objeto.save()
        ventas = Venta.objects.all()
        return render(request,"Venta.html",{"agregado":"si","ventas":ventas})
    else:
        ventas = Venta.objects.all()
        return render(request,"Venta.html",{"ventas":ventas})
