# Generated by Django 3.1.1 on 2020-10-26 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Vistas', '0003_remove_usuario_tipo'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='Tipo',
            field=models.IntegerField(default=0),
        ),
    ]
