from django.db import models
import datetime


Categorie = (
    
    ('acte_mariage', 'ACTE DE MARIAGE'),
    ('acte_naissance', 'ACTE DE NAISSANCE'),
)


# Create your models here.

class Mariage(models.Model):
    Requerant = (
        ('epoux(se)', 'EPOUX(se)'),
        ('conjoint(e)', 'CONJOINT(E)'),
    )

    Regime= (
        ('simple', 'SIMPLE'),
        ('communaute', 'COMUAUTE DE BIEN'),
    )

    categorie = models.IntegerField(choices=Categorie)
    numero = models.CharField(max_length=5, unique=True)
    requerant1 = models.CharField(max_length=500)
    profession_req1 = models.CharField(max_length=500)
    domicile_req1   = models.CharField(max_length=500)
    date_req1   = models.DateField()
    lieu_naiss_req1 = models.CharField(max_length=500)
    pere_req1 = models.CharField(max_length=250)
    mere_req1 = models.CharField(max_length=250)
    temoin_req1 = models.CharField(max_length=250)
    tel_temoin_req1 = models.CharField(max_length=250)
    profession_temoin_req1 = models.CharField(max_length=250)

    conjoint   = models.CharField(max_length=150, choices=Requerant)
    requerant2 = models.CharField(max_length=500)
    profession_req2 = models.CharField(max_length=500)
    domicile_req2 = models.CharField(max_length=500)
    date_req2 = models.DateField()
    lieu_naiss_req2 = models.CharField(max_length=500)
    pere_req2 = models.CharField(max_length=250)
    mere_req2 = models.CharField(max_length=250)
    temoin_req2 = models.CharField(max_length=250)
    tel_temoin_req2 = models.CharField(max_length=250)
    profession_temoin_req2 = models.CharField(max_length=250)
    regime = models.CharField(max_length=150,choices=Regime)
    date_mariage = models.DateField()
    heure_mariage = models.DateField()
    lieu_mariage = models.CharField(max_length=500)

    class Meta:
        db_table = "Actes_Mariage"
