from django.db import models

# Create your models here.
class Actividad (models.Model):
    Registro = models.CharField(max_length=20)
    IdUsuario = models.IntegerField(default=0)
    MovimientoAct = models.CharField(max_length=20)
    MovimientoTabla = models.CharField(max_length=20)

class Asistencia (models.Model):
    Fecha = models.DateField
    Idempleado = models.IntegerField(default=0)
    Hora = models.TimeField

class Balance (models.Model):
    FechaInicio = models.DateField
    FechaFinal = models.DateField
    Total = models.FloatField(default=0)

class Cliente (models.Model):
    Nombre = models.CharField(max_length=20)
    Direccion = models.CharField(max_length=50)
    Telefono = models.IntegerField(default=0)
    Correo = models.EmailField(max_length=20)
    ApellidoM = models.CharField(max_length=15)
    ApellidoP = models.CharField(max_length=15)
    Sexo = models.CharField(max_length=10)
    FechaNacimiento = models.DateField

class Compra (models.Model):
    Fecha = models.DateField
    Total = models.FloatField(default=0)
    TipoPago = models.CharField(max_length=20)
    IdCliente = models.IntegerField(default=0)

class DetalleCompra (models.Model):
    IdMateriaPrima = models.IntegerField(default=0)
    IdMateriaCompra = models.IntegerField(default=0)
    Cantidad = models.FloatField(default=0)

class Devoluciones (models.Model):
    Fecha = models.DateField
    Cantidad = models.IntegerField(default=0)
    Descripcion = models.TextField(max_length=100)
    IdProducto = models.IntegerField(default=0)

class Empleado (models.Model):
    Nombre = models.CharField(max_length=20)
    ApellidoP = models.CharField(max_length=20)
    ApellidoM = models.CharField(max_length=20)
    Correo = models.EmailField(max_length=40)
    Rfc = models.CharField(max_length=25)
    Telefono = models.IntegerField(default=0)
    Sexo = models.CharField(max_length=10)
    FechaIngreso = models.DateField
    Cargo = models.CharField(max_length=20)
    Salario = models.IntegerField(default=0)
    EstadoCivil = models.CharField(max_length=15)
    Nss = models.CharField(max_length=15)

class Evaluacion (models.Model):
    Tipo = models.CharField(max_length=20)
    Pregunta1 = models.CharField(max_length=70)
    Pregunta2 = models.CharField(max_length=70)
    Pregunta3 = models.CharField(max_length=70)
    Pregunta4 = models.CharField(max_length=70)
    Pregunta5 = models.CharField(max_length=70)
    Pregunta6 = models.CharField(max_length=70)
    Pregunta7 = models.CharField(max_length=70)
    Pregunta8 = models.CharField(max_length=70)
    Pregunta9 = models.CharField(max_length=70)
    Pregunta10 = models.CharField(max_length=70)

class Jornada (models.Model):
    HorasTrabajadas = models.IntegerField(default=0)
    DiasTrabajados = models.IntegerField(default=0)
    PagoHora = models.FloatField(default=0)
    HorasExtra = models.FloatField(default=0)
    Bonos = models.FloatField(default=0)
    IdEmpleado = models.IntegerField(default=0)

class Mantenimiento (models.Model):
    FechaMan = models.DateField
    Area = models.CharField(max_length=20)
    IdMob = models.IntegerField(default=0)
    CostoMan = models.FloatField(default=0)
    IdEmpleado = models.IntegerField(default=0)

class MateriaPrima (models.Model):
    Nombre = models.CharField(max_length=30)
    Tipo = models.CharField(max_length=20)
    Descripcion = models.CharField(max_length=70)
    Precio = models.IntegerField(default=0)
    Stock = models.IntegerField(default=0)
    Existencias = models.IntegerField(default=0)

class Mobiliario (models.Model):
    Nombre = models.CharField(max_length=20)
    Descripcion = models.CharField(max_length=50)
    Cantidad = models.IntegerField(default=0)
    Nic = models.IntegerField(default=0)
    Tipo = models.CharField(max_length=30)

class Pago (models.Model):
    IdEmpleado = models.IntegerField(default=0)
    Sal = models.IntegerField(default=0)
    FechaDep = models.DateField
    MetodoPago = models.CharField(max_length=30)
    Des = models.CharField(max_length=30)

class Pedido (models.Model):
    Fecha = models.DateField
    IdCliente = models.IntegerField(default=0)
    Precio = models.FloatField(default=0)
    Cantidad = models.FloatField(default=0)
    Direccion = models.CharField(max_length=50)
    IdProducto = models.IntegerField(default=0)

class Permisos (models.Model):
    IdUsuario = models.IntegerField(default=0)
    ActPermiso = models.BooleanField('Activada/No Activada', default = False)
    ActConsulta = models.BooleanField('Activada/No Activada', default = False)
    AsisPermiso = models.BooleanField('Activada/No Activada', default = False)
    AsisConsulta = models.BooleanField('Activada/No Activada', default = False)
    BalPermiso = models.BooleanField('Activada/No Activada', default = False)
    BalConsulta = models.BooleanField('Activada/No Activada', default = False)
    CliPermiso = models.BooleanField('Activada/No Activada', default = False)
    CliConsulta = models.BooleanField('Activada/No Activada', default = False)
    ComPermiso = models.BooleanField('Activada/No Activada', default = False)
    ComConsulta = models.BooleanField('Activada/No Activada', default = False)
    DcomPermiso = models.BooleanField('Activada/No Activada', default = False)
    DcomConsulta = models.BooleanField('Activada/No Activada', default = False)
    DevPermiso = models.BooleanField('Activada/No Activada', default = False)
    DevConsulta = models.BooleanField('Activada/No Activada', default = False)
    EmpPermiso = models.BooleanField('Activada/No Activada', default = False)
    EmpConsulta = models.BooleanField('Activada/No Activada', default = False)
    EvaPermiso = models.BooleanField('Activada/No Activada', default = False)
    EvaConsulta = models.BooleanField('Activada/No Activada', default = False)
    JorPermiso = models.BooleanField('Activada/No Activada', default = False)
    JorConsulta = models.BooleanField('Activada/No Activada', default = False)
    ManPermiso = models.BooleanField('Activada/No Activada', default = False)
    ManConsulta = models.BooleanField('Activada/No Activada', default = False)
    MatPermiso = models.BooleanField('Activada/No Activada', default = False)
    MatConsulta = models.BooleanField('Activada/No Activada', default = False)
    MobPermiso = models.BooleanField('Activada/No Activada', default = False)
    MobConsulta = models.BooleanField('Activada/No Activada', default = False)
    PagoPermiso = models.BooleanField('Activada/No Activada', default = False)
    PagoConsulta = models.BooleanField('Activada/No Activada', default = False)
    PedidoPermiso = models.BooleanField('Activada/No Activada', default = False)
    PedidoConsulta = models.BooleanField('Activada/No Activada', default = False)
    ProduPermiso = models.BooleanField('Activada/No Activada', default = False)
    ProduConsulta = models.BooleanField('Activada/No Activada', default = False)
    ProvePermiso = models.BooleanField('Activada/No Activada', default = False)
    ProveConsulta = models.BooleanField('Activada/No Activada', default = False)
    ProyePermiso = models.BooleanField('Activada/No Activada', default = False)
    ProyeConsulta = models.BooleanField('Activada/No Activada', default = False)
    RemPermiso = models.BooleanField('Activada/No Activada', default = False)
    RemConsulta = models.BooleanField('Activada/No Activada', default = False)
    UsuarioPermiso = models.BooleanField('Activada/No Activada', default = False)
    UsuarioConsulta = models.BooleanField('Activada/No Activada', default = False)
    VentaPermiso = models.BooleanField('Activada/No Activada', default = False)
    VentaConsulta = models.BooleanField('Activada/No Activada', default = False)

class Producto (models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    PrecioV = models.FloatField(default=0)
    PrecioC = models.FloatField(default=0)
    Cantidad = models.FloatField(default=0)
    CantMin = models.FloatField(default=0)
    CantMax = models.FloatField(default=0)
    Categoria = models.IntegerField(default=0)

class Proveedor (models.Model):
    Nombre = models.CharField(max_length=50)
    Telefono = models.IntegerField(default=0)
    Direccion = models.CharField(max_length=50)
    Correo = models.CharField(max_length=30)
    Rfc = models.CharField(max_length=30)

class Proyecto (models.Model):
    NombrePro = models.CharField(max_length=20)
    TipoPro = models.CharField(max_length=20)
    IdEmpleado = models.IntegerField(default=0)
    FechaIn = models.DateField
    FechaFin = models.DateField
    Descripcion = models.CharField(max_length=30)

class Remplazo (models.Model):
    IdMobiliario = models.IntegerField(default=0)
    Fecha = models.DateField
    Costo = models.FloatField(default=0)
    Descripcion = models.CharField(max_length=200)

class Usuario (models.Model):
    Nombre = models.CharField(max_length=50)
    Tipo = models.IntegerField(default=0)
    Password = models.CharField(max_length=20)

class Venta (models.Model):
    Fecha = models.DateField
    IdCliente = models.IntegerField(default=0)
    Total = models.FloatField(default=0)
    TipoPago = models.IntegerField(default=0)
