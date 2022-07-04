from django import forms
from Décés.models import Deces


class DecesForm(forms.ModelForm):  
    class Meta:  
        model = Deces  
        fields = "__all__"