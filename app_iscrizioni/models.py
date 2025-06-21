from django.db import models

class Iscrizione(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.IntegerField(null=True)
    timestamp = models.DateField(null=True)
    torneo = models.CharField(max_length=100,null=True)
    squadra = models.CharField(max_length=100,null=True)
    codice_fiscale = models.CharField(max_length=16,null=True)
    note = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    is_paid = models.BooleanField(default=False)


