from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator 

class Filiere(models.Model):
    nom = models.CharField(max_length=3)

    def __str__(self):
        return f"{self.nom}"

class Classe(models.Model):
    nom = models.CharField(max_length=3)
    filiere = models.ForeignKey(Filiere, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.nom}, {self.filiere}"

class Promotion(models.Model):
    annee_debut = models.PositiveSmallIntegerField(default=1900, validators=[MinValueValidator(1900)])
    annee_fin = models.PositiveSmallIntegerField(default=1900, validators=[MinValueValidator(1900)])
    filieres = models.ManyToManyField(Filiere)

    def __str__(self):
        return f"{self.annee_debut} {self.annee_fin}"

class Utilisateur(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    promotion = models.ForeignKey(Promotion, on_delete=models.CASCADE)
    abonnements = models.ManyToManyField('Utilisateur', blank=True, related_name='abonnements_utilisateur')
    banis = models.ManyToManyField('Utilisateur', blank=True, related_name='utilisateur_bannis')

    def __str__(self):
        return f"{self.user.get_full_name()}"