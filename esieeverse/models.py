from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.conf import settings
import os

class Filiere(models.Model):
    """
    Modèle représentant la table filière
    """
    nom = models.CharField(max_length=5)

    def __str__(self):
        return f"{self.nom}"

class Promotion(models.Model):
    """
    Modèle représentant la table promotion
    """
    nom = models.CharField(max_length=5)
    filieres = models.ManyToManyField(Filiere)

    def __str__(self):
        return f"{self.nom}"

class Utilisateur(models.Model):
    """
    Modèle représentant la table utilisateur
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE,blank=True, null=True)
    #promotion = models.CharField(max_length=150, blank=True, null=True)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE, blank=True, null=True)
    #filiere = models.CharField(max_length=150, blank=True, null=True)
    abonnements = models.ManyToManyField('Utilisateur', blank=True, related_name='abonnements_utilisateur')
    banis = models.ManyToManyField('Utilisateur', blank=True, related_name='utilisateur_bannis')
    photo_de_profile = models.ImageField(null=True, upload_to='media/')
    entreprise = models.CharField(max_length=100, blank=True)
    nom = models.CharField(max_length=150, blank=True, null=True)
    prenom = models.CharField(max_length=150, blank=True, null=True)


    def __str__(self):
        return f"{self.user.get_full_name()}"
