from django.db import models
from django.contrib.auth.models import User

class Filiere(models.Model):
    nom = models.TimeField(max_length=3)

class Classe(models.Model):
    nom = models.CharField(max_length=3)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)

class Promotion(models.Model):
    annee_debut = models.DateField(auto_now=True)
    annee_fin = models.DateField(auto_now=True)
    filieres = models.ManyToManyField(Filiere)

class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    abonnements = models.ManyToManyField('Utilisateur', blank=True, related_name='abonnements_utilisateur')
    banis = models.ManyToManyField('Utilisateur', blank=True, related_name='utilisateur_bannis')

