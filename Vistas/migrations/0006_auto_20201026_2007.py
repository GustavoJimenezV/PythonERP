# Generated by Django 3.1.1 on 2020-10-27 02:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('Vistas', '0005_auto_20201026_1945'),
    ]

    operations = [
        migrations.AddField(
            model_name='asistencia',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 5, 35, 176461, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='asistencia',
            name='Hora',
            field=models.TimeField(default=datetime.datetime(2020, 10, 27, 2, 5, 53, 864369, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='balance',
            name='FechaFinal',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 1, 377317, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='balance',
            name='FechaInicio',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 12, 990535, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='FechaNacimiento',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 22, 561410, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='compra',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 26, 388196, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='devoluciones',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 30, 889567, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='empleado',
            name='FechaIngreso',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 34, 418264, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='FechaMan',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 40, 850217, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pago',
            name='FechaDep',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 45, 40307, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pedido',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 48, 809018, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='FechaFin',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 54, 117027, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='proyecto',
            name='FechaIn',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 6, 57, 813467, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='remplazo',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 7, 1, 342161, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='venta',
            name='Fecha',
            field=models.DateField(default=datetime.datetime(2020, 10, 27, 2, 7, 14, 689064, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
