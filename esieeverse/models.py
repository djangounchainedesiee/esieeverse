from django.db import models

class Classe(models.Model):
    nom = models.TextField(max_length=3)

class Filiere(models.Model):
    nom = models.TimeField(max_length=3)

class Promotion(models.Model):
    annee_debut = models.DateField(auto_now=True)
    annee_fin = models.DateField(auto_now=True)

class FilPromo(models.Model):
    idFiliere = models.ForeignKey(Filiere, on_delete=models.DO_NOTHING)
    idPromotion = models.ForeignKey(Promotion, on_delete=models.DO_NOTHING)