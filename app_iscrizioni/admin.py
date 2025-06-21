from django.contrib import admin
from .models import Iscrizione

# Register your models here.

class IscrizioneAdmin(admin.ModelAdmin):
  list_display = ("last_name", "first_name", "torneo",)

admin.site.register(Iscrizione , IscrizioneAdmin)