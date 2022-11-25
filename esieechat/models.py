from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Conversation(models.Model):
    nom = models.CharField(max_length=20)

class Message(models.Model):
    contenu = models.TextField(max_length=125)
    date_heure = models.DateTimeField(auto_now=True)
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)

class ConvUtilisateur(models.Model):
    conversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
