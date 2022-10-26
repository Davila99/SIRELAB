from django.contrib import admin

# Register your models here.
from .models import Asignaturas
from .models import Laboratorios
from .models import Carreras
from .models import Docentes
from .models import Registros


admin.site.register(Asignaturas)
admin.site.register(Laboratorios)
admin.site.register(Carreras)
admin.site.register(Docentes)
admin.site.register(Registros) 