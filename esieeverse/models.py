from django.db import models

class Classe(models.Model):
    nom = models.CharField(max_length=3)

class Filiere(models.Model):
    nom = models.TimeField(max_length=3)

class Promotion(models.Model):
    annee_debut = models.DateField(auto_now=True)
    annee_fin = models.DateField(auto_now=True)

class FilPromo(models.Model):
    filiere = models.ForeignKey(Filiere, on_delete=models.DO_NOTHING)
    promotion = models.ForeignKey(Promotion, on_delete=models.DO_NOTHING)