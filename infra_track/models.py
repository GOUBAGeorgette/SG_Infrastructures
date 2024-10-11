from django.db import models

class Panne(models.Model):
    titre = models.CharField(max_length=100)
    details = models.TextField()  # Assure-toi que ce champ existe
    date_signalement = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=[
        ('en_attente', 'En attente'),
        ('resolue', 'Résolue'),
        ('en_cours', 'En cours'),
    ])

    def __str__(self):
        return self.titre
