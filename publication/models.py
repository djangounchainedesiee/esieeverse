from django.db import models
from esieeverse.models import Utilisateur
from django.db.models import Count

# Create your models here.
class Publication(models.Model):
    """
    Modèle représentant la table Publication
    """
    titre = models.CharField(max_length=125)
    contenu = models.TextField(max_length=300)
    date = models.DateTimeField(auto_now=True)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    likes = models.ManyToManyField(Utilisateur, related_name='likes_utilisateur', blank=True)
    dislikes = models.ManyToManyField(Utilisateur, related_name='dislikes_utilisateur', blank=True)
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)

class Evenement(models.Model):
    """
    Modèle représentant la table Evènement
    """
    titre = models.CharField(max_length=125)
    contenu = models.TextField(max_length=300)
    image = models.ImageField(null=True, blank=True, upload_to='media/')
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    utilisateur_inscrits = models.ManyToManyField(Utilisateur, blank=True, related_name='utilisateur_inscrits')
    auteur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='auteur')

    def total_votes(self) -> int:
        """Retourne le nombre de votes sur un évènement

        Returns:
            float: Retourne le nombre de votes sur un évènement
        """
        return sum([choix.utilisateurs.all().count() for choix in self.choix_set.all()])  

class Choix(models.Model):
    """
    Modèle représentant la table Choix
    """
    nom = models.CharField(max_length=10)
    evenement = models.ForeignKey(Evenement, on_delete=models.CASCADE)
    utilisateurs = models.ManyToManyField(Utilisateur, blank=True)

    def nb_utilisateurs(self) -> float:
        """Retourne le nombre de personne qui ont choisis ce choix 

        Returns:
            float: le nombre de personne qui ont choisis ce choix 
        """
        return self.utilisateurs.all().count()

    def pourcentage(self) -> float:
        """Retourne le pourcentage de personne qui ont choisis ce choix par rapport au nombre total de votes de l'évènement

        Returns:
            float: le pourcentage de vote de ce choix
        """
        return round((self.nb_utilisateurs() * 100) / self.evenement.total_votes())  if self.evenement.total_votes() != 0 else 0
    
    def __str__(self):
        return f"{self.nom}"

