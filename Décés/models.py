
from django.db import models

# Create your models here.

class Deces(models.Model):
    registre    = models.CharField(max_length=250)
    numéro      = models.CharField(max_length=500)
    prenom = models.CharField(max_length=50)
    nom = models.CharField(max_length=50)
    datenaiss    = models.CharField(max_length=100 ,blank=True)
    lieunaiss      = models.CharField(max_length=100, blank=True)
    
    class Meta:
        db_table = "acte_décés"