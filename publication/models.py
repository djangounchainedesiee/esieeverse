from django.db import models
from esieeverse.models import Utilisateur
from django.conf import settings
import os

# Create your models here.
class Publication(models.Model):
    """
    Modèle représentant la table Promotion
    """
    texte = models.CharField(max_length=125)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    likes = models.ManyToManyField(Utilisateur, related_name='likes_utilisateur', blank=True)
    dislikes = models.ManyToManyField(Utilisateur, related_name='dislikes_utilisateur', blank=True)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Evenement(Publication):
    """
    Modèle représentant la table Evènement
    """
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

class Choix(models.Model):
    """
    Modèle représentant la table Choix
    """
    nom = models.CharField(max_length=10)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['id', 'evenement', 'utilisateur'], name='unique_vote_user')
        ]

    def __str__(self):
        return f"{self.nom}"
