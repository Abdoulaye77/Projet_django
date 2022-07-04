from django import forms
from EtatCivil.models import Mariage


class MariageForm(forms.ModelForm):  
    class Meta:  
        model = Mariage  
        fields = "__all__"