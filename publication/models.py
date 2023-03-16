from django.db import models
from esieeverse.models import Utilisateur
from django.conf import settings
import os

# Create your models here.
class Publication(models.Model):
    """
    Modèle représentant la table Publication
    """
    titre = models.CharField(max_length=125)
    contenu = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    likes = models.ManyToManyField(Utilisateur, related_name='likes_utilisateur', blank=True)
    dislikes = models.ManyToManyField(Utilisateur, related_name='dislikes_utilisateur', blank=True)
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Evenement(models.Model):
    """
    Modèle représentant la table Evènement
    """
    titre = models.CharField(max_length=125)
    contenu = models.TextField(max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    utilisateur_inscrits = models.ManyToManyField(Utilisateur, blank=True, related_name='utilisateur_inscrits')
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='auteur')

class Choix(models.Model):
    """
    Modèle représentant la table Choix
    """
    nom = models.CharField(max_length=10)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    utilisateur = models.ManyToManyField(Utilisateur, blank=True)
    
    def __str__(self):
        return f"{self.nom}"
