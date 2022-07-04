from django.db import models

# Create your models here.

class Mairie(models.Model):
    Commune    = models.CharField(max_length=250)
    maire      = models.CharField(max_length=500)
    telephone1 = models.CharField(max_length=50)
    telephone2 = models.CharField(max_length=50)
    adresse    = models.CharField(max_length=100 ,blank=True)
    email      = models.CharField(max_length=100, blank=True)
    site       = models.CharField(max_length=100,  blank=True)
    logo       = models.ImageField(upload_to='logos', blank=True, null=True)
    class Meta:
        db_table = "str_mairie"