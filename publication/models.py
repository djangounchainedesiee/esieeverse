from django.db import models

# Create your models here.
class Publication(models.Model):
    texte = models.CharField(max_length=125)
    date = models.DateTimeField(auto_now=True)
    contien_multimedia = models.BooleanField(default=False)
    nb_likes = models.PositiveSmallIntegerField(default=0)
    nb_dislikes = models.PositiveSmallIntegerField(default=0)

class Evenement(Publication):
    date_debut = models.DateTimeField(auto_now=True)
    date_fin = models.DateTimeField()

class Choix(models.Model):
    nom = models.CharField(max_length=10)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    nb_choisis = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.nom}"
