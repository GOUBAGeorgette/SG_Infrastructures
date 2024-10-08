from django.db import models

class Panne(models.Model):
    titre = models.CharField(max_length=255)  # Exemple de champ
    details = models.TextField()                # Exemple de champ
    date_signalement = models.DateTimeField(auto_now_add=True)  # Champ pour la date
