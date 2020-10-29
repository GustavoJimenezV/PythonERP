from django.shortcuts import render
from django.http import HttpResponse
from django.template import Template,Context
from django.template import loader
from Vistas.models import *
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


def MenuActividad(request):
    if request.POST:
        objeto = Actividad()
        objeto.Registro = request.POST["Registro"]
        objeto.IdUsuario = request.POST["IdUsuario"]
        objeto.MovimientoAct = request.POST["MovimientoAct"]
        objeto.MovimientoTabla = request.POST["MovimientoTabla"]
        objeto.save()
        actividades = Actividad.objects.all()
        return render(request,"Actividad.html",{"agregado":"si","actividades":actividades})
    else:
        actividades = Actividad.objects.all()
        return render(request,"Actividad.html",{"actividades":actividades})

def MenuAsistencia(request):
    if request.POST:
        objeto = Asistencia()
        objeto.IdEmpleado = request.POST["IdEmpleado"]
        objeto.Fecha = request.POST["Fecha"]
        objeto.Hora = request.POST["Hora"]
        objeto.save()
        asistencias = Asistencia.objects.all()
        return render(request,"Asistencia.html",{"agregado":"si","asistencias":asistencias})
    else:
        asistencias = Asistencia.objects.all()
        return render(request,"Asistencia.html",{"asistencias":asistencias})

def MenuBalance(request):
    if request.POST:
        objeto = Balance()
        objeto.Total = request.POST["Total"]
        objeto.FechaFinal = request.POST["FechaFinal"]
        objeto.FechaInicio = request.POST["FechaInicio"]
        objeto.save()
        balances = Balance.objects.all()
        return render(request,"Balance.html",{"agregado":"si","balances":balances})
    else:
        balances = Balance.objects.all()
        return render(request,"Balance.html",{"balances":balances})

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

def MenuCompra(request):
    if request.POST:
        objeto = Compra()
        objeto.Total = request.POST["Total"]
        objeto.TipoPago = request.POST["TipoPago"]
        objeto.IdCliente = request.POST["IdCliente"]
        objeto.Fecha = request.POST["Fecha"]
        objeto.save()
        compras = Compra.objects.all()
        return render(request,"Compra.html",{"agregado":"si","compras":compras})
    else:
        compras = Compra.objects.all()
        return render(request,"Compra.html",{"compras":compras})

def GraficaCompra(request):
    objeto = Compra()
    compras = Compra.objects.all()
    return render (request,"GraficaCompra.html",{"compras":compras})

def MenuDetalleCompra(request):
    if request.POST:
        objeto = DetalleCompra()
        objeto.IdMateriaPrima = request.POST["IdMateriaPrima"]
        objeto.IdMateriaCompra = request.POST["IdMateriaCompra"]
        objeto.Cantidad = request.POST["Cantidad"]
        objeto.save()
        detallecompras = DetalleCompra.objects.all()
        return render(request,"DetalleCompra.html",{"agregado":"si","detallecompras":detallecompras})
    else:
        detallecompras = DetalleCompra.objects.all()
        return render(request,"DetalleCompra.html",{"detallecompras":detallecompras})

def MenuDevolucion(request):
    if request.POST:
        objeto = Devolucion()
        objeto.Cantidad = request.POST["Cantidad"]
        objeto.Descripcion = request.POST["Descripcion"]
        objeto.IdProducto = request.POST["IdProducto"]
        objeto.Fecha = request.POST["Fecha"]
        objeto.save()
        devoluciones = Devolucion.objects.all()
        return render(request,"Devolucion.html",{"agregado":"si","devoluciones":devoluciones})
    else:
        devoluciones = Devolucion.objects.all()
        return render(request,"Devolucion.html",{"devoluciones":devoluciones})

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

def MenuEvaluacion(request):
    if request.POST:
        objeto = Evaluacion()
        objeto.Tipo = request.POST["Tipo"]
        objeto.Pregunta1 = request.POST["Pregunta1"]
        objeto.Pregunta2 = request.POST["Pregunta2"]
        objeto.Pregunta3 = request.POST["Pregunta3"]
        objeto.Pregunta4 = request.POST["Pregunta4"]
        objeto.Pregunta5 = request.POST["Pregunta5"]
        objeto.Pregunta6 = request.POST["Pregunta6"]
        objeto.Pregunta7 = request.POST["Pregunta7"]
        objeto.Pregunta8 = request.POST["Pregunta8"]
        objeto.Pregunta9 = request.POST["Pregunta9"]
        objeto.Pregunta10 = request.POST["Pregunta10"]
        objeto.save()
        evaluaciones = Evaluacion.objects.all()
        return render(request,"Evaluacion.html",{"agregado":"si","evaluaciones":evaluaciones})
    else:
        evaluaciones = Evaluacion.objects.all()
        return render(request,"Evaluacion.html",{"evaluaciones":evaluaciones})

def MenuJornada(request):
    if request.POST:
        objeto = Jornada()
        objeto.HorasTrabajadas = request.POST["HorasTrabajadas"]
        objeto.DiasTrabajados = request.POST["DiasTrabajados"]
        objeto.PagoHora = request.POST["PagoHora"]
        objeto.HorasExtra = request.POST["HorasExtra"]
        objeto.Bonos = request.POST["Bonos"]
        objeto.IdEmpleado = request.POST["IdEmpleado"]
        objeto.save()
        jornadas = Jornada.objects.all()
        return render(request,"Jornada.html",{"agregado":"si","jornadas":jornadas})
    else:
        jornadas = Jornada.objects.all()
        return render(request,"Jornada.html",{"jornadas":jornadas})

def MenuMantenimiento(request):
    if request.POST:
        objeto = Mantenimiento()
        objeto.FechaMan = request.POST["FechaMantenimiento"]
        objeto.Area = request.POST["Area"]
        objeto.IdMob = request.POST["IdMobiliario"]
        objeto.CostoMan = request.POST["CostoMantenimiento"]
        objeto.IdEmpleado = request.POST["IdEmpleado"]
        objeto.save()
        mantenimientos = Mantenimiento.objects.all()
        return render(request,"Mantenimiento.html",{"agregado":"si","mantenimientos":mantenimientos})
    else:
        mantenimientos = Mantenimiento.objects.all()
        return render(request,"Mantenimiento.html",{"mantenimientos":mantenimientos})

def MenuMateriaPrima(request):
    if request.POST:
        objeto = MateriaPrima()
        objeto.Nombre = request.POST["Nombre"]
        objeto.Tipo = request.POST["Tipo"]
        objeto.Descripcion = request.POST["Descripcion"]
        objeto.Precio = request.POST["Precio"]
        objeto.Stock = request.POST["Stock"]
        objeto.Existencia = request.POST["Existencia"]
        objeto.save()
        materiaprimas = MateriaPrima.objects.all()
        return render(request,"MateriaPrima.html",{"agregado":"si","materiaprimas":materiaprimas})
    else:
        materiaprimas = MateriaPrima.objects.all()
        return render(request,"MateriaPrima.html",{"materiaprimas":materiaprimas})

def GraficaMateriaPrima(request):
    objeto = MateriaPrima()
    materiaprimas = MateriaPrima.objects.all()
    return render (request,"GraficaMateriaPrima.html",{"materiaprimas":materiaprimas})

def MenuMobiliario(request):
    if request.POST:
        objeto = Mobiliario()
        objeto.Nombre = request.POST["Nombre"]
        objeto.Descripcion = request.POST["Descripcion"]
        objeto.Cantidad = request.POST["Cantidad"]
        objeto.Nic = request.POST["Nic"]
        objeto.Tipo = request.POST["Tipo"]
        objeto.save()
        mobiliarios = Mobiliario.objects.all()
        return render(request,"Moviliario.html",{"agregado":"si","mobiliarios":mobiliarios})
    else:
        mobiliarios = Mobiliario.objects.all()
        return render(request,"Mobiliario.html",{"mobiliarios":mobiliarios})

def MenuPago(request):
    if request.POST:
        objeto = Pago()
        objeto.IdEmpleado = request.POST["IdEmpleado"]
        objeto.Sal = request.POST["Sal"]
        objeto.FechaDep = request.POST["FechaDep"]
        objeto.MetodoPago = request.POST["MetodoPago"]
        objeto.Des = request.POST["Des"]
        objeto.save()
        pagos = Pago.objects.all()
        return render(request,"Pago.html",{"agregado":"si","pagos":pagos})
    else:
        pagos = Pago.objects.all()
        return render(request,"Pago.html",{"pagos":pagos})

def MenuPedido(request):
    if request.POST:
        objeto = Pedido()
        objeto.Fecha = request.POST["Fecha"]
        objeto.IdCliente = request.POST["IdCliente"]
        objeto.Precio = request.POST["Precio"]
        objeto.Cantidad = request.POST["Cantidad"]
        objeto.Direccion = request.POST["Direccion"]
        objeto.IdProducto = request.POST["IdProducto"]
        objeto.save()
        pedidos = Pedido.objects.all()
        return render(request,"Pedido.html",{"agregado":"si","pedidos":pedidos})
    else:
        pedidos = Pedido.objects.all()
        return render(request,"Pedido.html",{"pedidos":pedidos})

def GraficaPedido(request):
    objeto = Pedido()
    pedidos = Pedido.objects.all()
    return render (request,"GraficaPedido.html",{"pedidos":pedidos})

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
        objeto.Cantidad = request.POST["Cantidad"]
        objeto.CantMin = request.POST["CantidadMin"]
        objeto.CantMax = request.POST["CantidadMax"]
        objeto.Categoria = request.POST["Categoria"]
        objeto.save()
        productos = Producto.objects.all()
        return render(request,"Producto.html",{"agregado":"si","productos":productos})
    else:
        productos = Producto.objects.all()
        return render(request,"Producto.html",{"productos":productos})

def GraficaProducto(request):
    objeto = Producto()
    productos = Producto.objects.all()
    return render (request,"GraficaProducto.html",{"productos":productos})

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

def GraficaVenta(request):
    objeto = Venta()
    ventas = Venta.objects.all()
    return render (request,"GraficaVenta.html",{"ventas":ventas})
