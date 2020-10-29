from django.db import models

# Create your models here.

class Actividad (models.Model):
    IdUsuario = models.IntegerField(default=0)
    Registro = models.CharField(max_length=20)
    MovimientoAct = models.CharField(max_length=20)
    MovimientoTabla = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Actividad'
        verbose_name_plural = 'Actividades'
        ordering = ['Registro']
    def __str__(self):
        return self.Registro

class Asistencia (models.Model):
    IdEmpleado = models.IntegerField(default=0)
    Fecha = models.DateField()
    Hora = models.TimeField(auto_now_add=False, auto_now=False)
    class Meta:
        verbose_name = 'Asistencia'
        verbose_name_plural = 'Asistencias'
        ordering = ['IdEmpleado']
    def __str__(self):
        return self.IdEmpleado

class Balance (models.Model):
    FechaInicio = models.DateField()
    FechaFinal = models.DateField()
    Total = models.FloatField(default=0)
    class Meta:
        verbose_name = 'Balance'
        verbose_name_plural = 'Balances'
        ordering = ['FechaInicio']
    def __str__(self):
        return self.FechaInicio

class Cliente (models.Model):
    Nombre = models.CharField(max_length=20)
    ApellidoP = models.CharField(max_length=15)
    ApellidoM = models.CharField(max_length=15)
    Direccion = models.CharField(max_length=50)
    Telefono = models.IntegerField(default=0)
    Correo = models.EmailField(max_length=20)
    Sexo = models.CharField(max_length=10)
    FechaNacimiento = models.DateField()
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        ordering = ['Nombre']
    def __str__(self):
        return self.Nombre

class Compra (models.Model):
    IdCliente = models.IntegerField(default=0)
    Fecha = models.DateField()
    Total = models.FloatField(default=0)
    TipoPago = models.CharField(max_length=20)
    class Meta:
        verbose_name = 'Compra'
        verbose_name_plural = 'Compras'
        ordering = ['Fecha']
    def __str__(self):
        return self.Fecha

class DetalleCompra (models.Model):
    IdMateriaPrima = models.IntegerField(default=0)
    IdMateriaCompra = models.IntegerField(default=0)
    Cantidad = models.FloatField(default=0)
    class Meta:
        verbose_name = 'DetalleCompra'
        verbose_name_plural = 'DetalleCompras'
        ordering = ['IdMateriaPrima']
    def __str__(self):
        return self.IdMateriaPrima

class Devolucion (models.Model):
    Fecha = models.DateField()
    Cantidad = models.IntegerField(default=0)
    Descripcion = models.TextField(max_length=100)
    IdProducto = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Devolucion'
        verbose_name_plural = 'Devoluciones'
        ordering = ['Fecha']
    def __str__(self):
        return self.Fecha

class Empleado (models.Model):
    Nombre = models.CharField(max_length=20)
    ApellidoP = models.CharField(max_length=20)
    ApellidoM = models.CharField(max_length=20)
    Correo = models.EmailField(max_length=40)
    Rfc = models.CharField(max_length=25)
    Telefono = models.IntegerField(default=0)
    Sexo = models.CharField(max_length=10)
    FechaIngreso = models.DateField()
    Cargo = models.CharField(max_length=20)
    Salario = models.IntegerField(default=0)
    EstadoCivil = models.CharField(max_length=15)
    Nss = models.CharField(max_length=15)
    class Meta:
        verbose_name = 'Empleado'
        verbose_name_plural = 'Empleados'
        ordering = ['Nombre']
    def __str__(self):
        return self.Nombre

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
    class Meta:
        verbose_name = 'Evaluacion'
        verbose_name_plural = 'Evaluaciones'
        ordering = ['Tipo']
    def __str__(self):
        return self.Tipo

class Jornada (models.Model):
    HorasTrabajadas = models.IntegerField(default=0)
    DiasTrabajados = models.IntegerField(default=0)
    PagoHora = models.FloatField(default=0)
    HorasExtra = models.FloatField(default=0)
    Bonos = models.FloatField(default=0)
    IdEmpleado = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Jornada'
        verbose_name_plural = 'Jornadas'
        ordering = ['IdEmpleado']
    def __str__(self):
        return self.IdEmpleado

class Mantenimiento (models.Model):
    FechaMan = models.DateField()
    Area = models.CharField(max_length=20)
    IdMob = models.IntegerField(default=0)
    CostoMan = models.FloatField(default=0)
    IdEmpleado = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Mantenimiento'
        verbose_name_plural = 'Mantenimientos'
        ordering = ['Area']
    def __str__(self):
        return self.Area

class MateriaPrima (models.Model):
    Nombre = models.CharField(max_length=30)
    Tipo = models.CharField(max_length=20)
    Descripcion = models.CharField(max_length=70)
    Precio = models.IntegerField(default=0)
    Stock = models.IntegerField(default=0)
    Existencia = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'MateriaPrima'
        verbose_name_plural = 'MateriaPrimas'
        ordering = ['Nombre']
    def __str__(self):
        return self.Nombre

class Mobiliario (models.Model):
    Nombre = models.CharField(max_length=20)
    Descripcion = models.CharField(max_length=50)
    Cantidad = models.IntegerField(default=0)
    Nic = models.IntegerField(default=0)
    Tipo = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Mobiliario'
        verbose_name_plural = 'Mobiliarios'
        ordering = ['Nombre']
    def __str__(self):
        return self.Nombre

class Pago (models.Model):
    IdEmpleado = models.IntegerField(default=0)
    Sal = models.IntegerField(default=0)
    FechaDep = models.DateField()
    MetodoPago = models.CharField(max_length=30)
    Des = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Pago'
        verbose_name_plural = 'Pagos'
        ordering = ['IdEmpleado']
    def __str__(self):
        return self.IdEmpleado

class Pedido (models.Model):
    Fecha = models.DateField()
    IdCliente = models.IntegerField(default=0)
    Precio = models.FloatField(default=0)
    Cantidad = models.FloatField(default=0)
    Direccion = models.CharField(max_length=50)
    IdProducto = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['Fecha']
    def __str__(self):
        return self.Fecha

class Permiso (models.Model):
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
    class Meta:
        verbose_name = 'Permiso'
        verbose_name_plural = 'Permisos'
        ordering = ['IdUsuario']
    def __str__(self):
        return self.IdUsuario

class Producto (models.Model):
    Nombre = models.CharField(max_length=50)
    Descripcion = models.CharField(max_length=50)
    PrecioV = models.FloatField(default=0)
    PrecioC = models.FloatField(default=0)
    Cantidad = models.FloatField(default=0)
    CantMin = models.FloatField(default=0)
    CantMax = models.FloatField(default=0)
    Categoria = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['Nombre']
    def __str__(self):
        return self.Nombre

class Proveedor (models.Model):
    Nombre = models.CharField(max_length=50)
    Telefono = models.IntegerField(default=0)
    Direccion = models.CharField(max_length=50)
    Correo = models.CharField(max_length=30)
    Rfc = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Proveedor'
        verbose_name_plural = 'Proveedores'
        ordering = ['Nombre']
    def __str__(self):
        return self.Nombre

class Proyecto (models.Model):
    NombrePro = models.CharField(max_length=20)
    TipoPro = models.CharField(max_length=20)
    IdEmpleado = models.IntegerField(default=0)
    FechaIn = models.DateField()
    FechaFin = models.DateField()
    Descripcion = models.CharField(max_length=30)
    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['NombrePro']
    def __str__(self):
        return self.NombrePro

class Remplazo (models.Model):
    IdMobiliario = models.IntegerField(default=0)
    Fecha = models.DateField()
    Costo = models.FloatField(default=0)
    Descripcion = models.CharField(max_length=200)
    class Meta:
        verbose_name = 'Remplazo'
        verbose_name_plural = 'Remplazos'
        ordering = ['Descripcion']
    def __str__(self):
        return self.Descripcion

class Usuario (models.Model):
    Nombre = models.CharField(max_length=50)
    Password = models.CharField(max_length=20)
    Tipo = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        ordering = ['Nombre']
    def __str__(self):
        return self.Nombre

class Venta (models.Model):
    Fecha = models.DateField()
    IdCliente = models.IntegerField(default=0)
    Total = models.FloatField(default=0)
    TipoPago = models.IntegerField(default=0)
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['Fecha']
    def __str__(self):
        return self.Fecha
