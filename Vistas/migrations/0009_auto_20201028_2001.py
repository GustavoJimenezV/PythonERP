# Generated by Django 3.1.1 on 2020-10-29 02:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Vistas', '0008_auto_20201028_1947'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Devoluciones',
            new_name='Devolucion',
        ),
        migrations.AlterModelOptions(
            name='devolucion',
            options={'ordering': ['Fecha'], 'verbose_name': 'Devolucion', 'verbose_name_plural': 'Devoluciones'},
        ),
        migrations.AlterModelOptions(
            name='evaluacion',
            options={'ordering': ['Tipo'], 'verbose_name': 'Evaluacion', 'verbose_name_plural': 'Evaluaciones'},
        ),
        migrations.AlterModelOptions(
            name='jornada',
            options={'ordering': ['IdEmpleado'], 'verbose_name': 'Jornada', 'verbose_name_plural': 'Jornadas'},
        ),
        migrations.AlterModelOptions(
            name='mantenimiento',
            options={'ordering': ['Area'], 'verbose_name': 'Mantenimiento', 'verbose_name_plural': 'Mantenimientos'},
        ),
        migrations.AlterModelOptions(
            name='materiaprima',
            options={'ordering': ['Nombre'], 'verbose_name': 'MateriaPrima', 'verbose_name_plural': 'MateriaPrimas'},
        ),
    ]
