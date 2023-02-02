from django.db import models
from esieeverse.models import Utilisateur
from django.conf import settings
import os

# Create your models here.
class Publication(models.Model):
    texte = models.CharField(max_length=125)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True)
    nb_likes = models.PositiveSmallIntegerField(default=0)
    nb_dislikes = models.PositiveSmallIntegerField(default=0)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
class Evenement(Publication):
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()

class Choix(models.Model):
    nom = models.CharField(max_length=10)
    nb_choisis = models.IntegerField(default=0)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    
    class Meta:
        constraints=[
            models.UniqueConstraint(fields=['id', 'evenement', 'utilisateur'], name='unique_vote_user')
        ]

    def __str__(self):
        return f"{self.nom}"
