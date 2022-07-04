from __future__ import unicode_literals

from django.db import models
import datetime
# Create your models here.
class Naissance(models.Model):
    Categorie = (
    
    ('acte_mariage', 'ACTE DE MARIAGE'),
    ('acte_naissance', 'ACTE DE NAISSANCE'),
    )
    
    YEAR_CHOICES = []
    for r in range(1900, (datetime.datetime.now().year + 1)):
        YEAR_CHOICES.append((r, r))

    Sexe = (
        ('M', 'Masculin'),
        ('F', 'Feminin'),
    )

    # Infos Gles
    numero_registre = models.CharField(max_length=150)
    annee = models.IntegerField( choices=YEAR_CHOICES,
                                default=datetime.datetime.now().year)
    categorie = models.CharField(max_length=150, choices=Categorie)
    #centre = models.ForeignKey(Centre)

    # informations recipiendaire
    sexe = models.CharField(max_length=150, choices=Sexe)
    nom = models.CharField(max_length=250)
    prenoms = models.CharField(max_length=250)
    date_naiss = models.DateField()
    heure_naiss = models.TimeField()
    #hopital = models.ForeignKey(Centre,on_delete=models.CASCADE)

    # parents
    pere = models.CharField(max_length=250, blank=True)
    profession_pere = models.CharField(max_length=250, blank=True)
    mere = models.CharField(max_length=250)
    profession_mere = models.CharField(max_length=250)
    ajouter_le = models.DateField(auto_now_add=False)
    modifier_le = models.DateField(auto_now_add=False)

    class Meta:
        db_table = "Actes_Naissance"
