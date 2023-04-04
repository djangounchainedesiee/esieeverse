from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator
from django.conf import settings
import os

class Filiere(models.Model):
    """
    Modèle représentant la table filière
    """
    nom = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.nom}"

class Classe(models.Model):
    """
    Modèle représentant la table classe
    """
    nom = models.CharField(max_length=3)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom}, {self.filiere}"

class Promotion(models.Model):
    """
    Modèle représentant la table promotion
    """
    annee_fin = models.PositiveSmallIntegerField(default=1900, validators=[MinValueValidator(1900)])
    filieres = models.ManyToManyField(Filiere)

    def __str__(self):
        return f"{self.annee_fin}"

class Utilisateur(models.Model):
    """
    Modèle représentant la table utilisateur
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    classe = models.ForeignKey(Classe, on_delete=models.CASCADE)
    abonnements = models.ManyToManyField('Utilisateur', blank=True, related_name='abonnements_utilisateur')
    banis = models.ManyToManyField('Utilisateur', blank=True, related_name='utilisateur_bannis')
    photo_de_profile = models.ImageField(null=True, upload_to='media/')

    def __str__(self):
        return f"{self.user.get_full_name()}"
