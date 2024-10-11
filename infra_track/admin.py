from django.contrib import admin
from .models import Panne

class PanneAdmin(admin.ModelAdmin):
    list_display = ('titre', 'date_signalement', 'status')  # Champs à afficher dans la liste
    search_fields = ('titre',)  # Permet la recherche par titre
    list_filter = ('status',)  # Permet le filtrage par statut

# Enregistrement du modèle avec la classe d'administration personnalisée
admin.site.register(Panne, PanneAdmin)
