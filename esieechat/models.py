from django.db import models
from esieeverse.models import Utilisateur

# Create your models here.

class Conversation(models.Model):
    """
    Représente la table conversation
    """
    nom = models.CharField(max_length=20)
    utilisateurs = models.ManyToManyField(Utilisateur)

    def __str__(self) -> str:
        return f"{self.nom}"

class Message(models.Model):
    """
    Représente la table conversation
    """
    contenu = models.TextField(max_length=125)
    date_heure = models.DateTimeField(auto_now=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
