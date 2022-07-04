from django.contrib import admin

# Register your models here.
from EtatcivilNaiss.models import Naissance
from EtatcivilNaiss.forms import NaissanceForm
# Register your models here.

admin.site.register(Naissance)
