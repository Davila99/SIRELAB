from django.db import models

class Asignaturas(models.Model):
    descripcion = models.CharField(max_length=200)
class Laboratorios(models.Model):
    descripcion = models.CharField(max_length=200)
class Carreras(models.Model):
    descripcion = models.CharField(max_length=200) 
    
class Docentes(models.Model):
    nombre = models.CharField(max_length=200)
    asignatura_id = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)
    
class Registros(models.Model):
    fecha = models.DateTimeField('date published')
    docentes_id = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    laboratorio_id = models.ForeignKey(Laboratorios, on_delete=models.CASCADE)
    carreras_id = models.ForeignKey(Carreras, on_delete=models.CASCADE)
    hora_inicio = models.DateTimeField('date published')
    hora_fin = models.DateTimeField('date published')
    