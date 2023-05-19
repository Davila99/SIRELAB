import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'SIRELAB.settings')
django.setup()

from django.contrib.auth.models import User

# Crea el superusuario
superuser = User.objects.create_superuser(username="admin", email="admin@admin", password="admin")

print("Superusuario creado exitosamente.")
