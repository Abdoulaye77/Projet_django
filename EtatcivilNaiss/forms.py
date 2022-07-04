from django import forms
from EtatcivilNaiss.models import Naissance


class NaissanceForm(forms.ModelForm):  
    class Meta:  
        model = Naissance  
        fields = "__all__"
        """widgets = {
            'numero_registre': forms.TextInput(attrs={'class':'form-control'}),
            'annee': forms.TextInput(attrs={'class':'form-control'}),
            'categorie': forms.TextInput(attrs={'class':'form-control'}),
            'sexe': forms.TextInput(attrs={'class':'form-control'}),
            'nom': forms.TextInput(attrs={'class':'form-control'}),
            'prenoms': forms.TextInput(attrs={'class':'form-control'}),
            'date_naiss': forms.TextInput(attrs={'class':'form-control'}),
            'heure_naiss': forms.TextInput(attrs={'class':'form-control'}),
            'pere_req1': forms.TextInput(attrs={'class':'form-control'}),
            'pere': forms.TextInput(attrs={'class':'form-control'}),
            'profession_pere': forms.TextInput(attrs={'class':'form-control'}),
            'mere': forms.TextInput(attrs={'class':'form-control'}),
            'profession_mere': forms.TextInput(attrs={'class':'form-control'}),
            'ajouter_le': forms.TextInput(attrs={'class':'form-control'}),
            'modifier_le': forms.TextInput(attrs={'class':'form-control'}),
            
        }"""