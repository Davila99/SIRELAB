# Generated by Django 4.1.2 on 2022-10-26 18:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asignaturas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Carreras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Docentes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('asignatura_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.asignaturas')),
            ],
        ),
        migrations.CreateModel(
            name='Laboratorios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Registros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha', models.DateTimeField(verbose_name='date published')),
                ('hora_inicio', models.DateTimeField(verbose_name='date published')),
                ('hora_fin', models.DateTimeField(verbose_name='date published')),
                ('carreras_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.carreras')),
                ('docentes_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.docentes')),
                ('laboratorio_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='registro.laboratorios')),
            ],
        ),
    ]