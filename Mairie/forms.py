from django import forms
from Mairie.models import Mairie


class MairieForm(forms.ModelForm):  
    class Meta:  
        model = Mairie  
        fields = "__all__"