from django.db import models
from django.utils.text import slugify

class Iscrizione(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    data_di_nascita = models.DateField(null=True)
    luogo_di_nascita = models.CharField(max_length=100, null=True)
    phone = models.CharField(max_length=20, null=True)
    comune_residenza = models.CharField(max_length=100, null=True)
    indirizzo = models.CharField(max_length=255, null=True)
    numero_documento = models.CharField(max_length=50, null=True)
    ente_rilasciatore = models.CharField(max_length=100, null=True)
    data_rilascio = models.DateField(null=True)
    timestamp = models.DateField(null=True)
    torneo = models.CharField(max_length=100, null=True)
    squadra = models.CharField(max_length=100, null=True)
    codice_fiscale = models.CharField(max_length=16, null=True)
    note = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    pagato = models.BooleanField(default=False, null=False)
    slug = models.SlugField(default="", null=False)

    def __str__(self):
        return f"{self.last_name} {self.first_name} {self.torneo}"

    class Meta:
        verbose_name = "Iscrizione"
        verbose_name_plural = "Iscrizioni"

    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(f"{self.first_name}-{self.last_name}-{self.squadra}-{self.torneo}")
            slug = base_slug
            counter = 1
            while Iscrizione.objects.filter(slug=slug).exclude(pk=self.pk).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)