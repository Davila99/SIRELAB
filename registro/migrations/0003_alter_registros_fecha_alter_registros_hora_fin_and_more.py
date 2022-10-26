# Generated by Django 4.1.2 on 2022-10-26 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro', '0002_alter_registros_fecha_alter_registros_hora_fin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registros',
            name='fecha',
            field=models.DateField(verbose_name='Fecha'),
        ),
        migrations.AlterField(
            model_name='registros',
            name='hora_fin',
            field=models.TimeField(verbose_name='Hora Salida'),
        ),
        migrations.AlterField(
            model_name='registros',
            name='hora_inicio',
            field=models.TimeField(verbose_name='Hora Entrada'),
        ),
    ]
