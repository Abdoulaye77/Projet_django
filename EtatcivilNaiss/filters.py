from EtatcivilNaiss.models import django_filters
from .models import *

class NaissnceFilter(django_filters.FilterSet):
    class meta:
        model = Naissance
        fields = '__all__'
