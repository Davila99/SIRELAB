from django.db import models

class Asignaturas(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion
class Laboratorios(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion
class Carreras(models.Model):
    descripcion = models.CharField(max_length=200)
    def __str__(self):
        return self.descripcion
    
class Docentes(models.Model):
    nombre = models.CharField(max_length=200)
    asignatura_id = models.ForeignKey(Asignaturas, on_delete=models.CASCADE)
    def __str__(self):
        return self.nombre
    
class Registros(models.Model):
    fecha = models.DateField('Fecha')
    docentes_id = models.ForeignKey(Docentes, on_delete=models.CASCADE)
    laboratorio_id = models.ForeignKey(Laboratorios, on_delete=models.CASCADE)
    carreras_id = models.ForeignKey(Carreras, on_delete=models.CASCADE)
    hora_inicio = models.TimeField('Hora Entrada')
    hora_fin = models.TimeField('Hora Salida')
    def __str__(self):
         return self.fecha.strftime('%Y-%m-%d')
    