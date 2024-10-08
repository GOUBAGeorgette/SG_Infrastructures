from django import forms
from .models import Panne

class SignalementPanneForm(forms.ModelForm):
    class Meta:
        model = Panne
        fields = ['titre', 'details']  # Liste des champs à utiliser
