from django import forms
from .models import Panne

class PanneForm(forms.ModelForm):
    class Meta:
        model = Panne
        fields = ['description', 'infrastructure']  # Assure-toi que 'infrastructure' est défini dans ton modèle

