import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "portale_festantonio.settings")
django.setup()

from app_iscrizioni.models import Iscrizione

for x in Iscrizione.objects.filter(slug=""):
    x.pagato = False
    x.save()
    
    print(f"Aggiornato: {x}")