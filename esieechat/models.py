from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Message(models.Model):
    contenu = models.TextField(max_length=125)
    dateHeure = models.DateTimeField(auto_now=True)

class Conversation(models.Model):
    nom = models.TextField(max_length=20)

class ConvUtilisateur(models.Model):
    idConversation = models.ForeignKey(Conversation, on_delete=models.CASCADE)
    idUtilisateur = models.ForeignKey(User, on_delete=models.DO_NOTHING)
