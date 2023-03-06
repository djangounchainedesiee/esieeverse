from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from publication.models import Publication
from esieeverse.models import Utilisateur
import requests

def home_view(request: HttpRequest) -> HttpResponse:
    """Génère la vue principale contenant le flux d'actualité de la personne

    Args:
        request (HttpRequest): La requête

    Returns:
        HttpResponse: Affiche la vue de la page principale
    """
    publications = Publication.objects.filter(auteur_id__in=request.user.utilisateur.abonnements.all()).exclude(auteur_id=request.user.utilisateur)
    
    context = {
        'publications': publications,
    }

    return render(request,"home/index.html", context)

def add_friend(request: HttpRequest, utilisateur_id) -> HttpResponseRedirect:
    """Ajoute un ami à l'utilisateur

    Args:
        request (HttpRequest): La requête
        utilisateur_id (_type_): L'id de l'utilisateur à ajouter

    Returns:
        HttpResponseRedirect: Redirige vers la vue principale
    """
    utilisateur: Utilisateur = request.user.utilisateur
    response = requests.post(
        reverse('api:api_abonnements'), 
        data={'utilisateur_id': utilisateur.id, 'abonnement_id': utilisateur_id}, 
        cookies={'csrftoken': '<your_csrf_token_here>'}
    )


    
    utilisateurs_to_add = Utilisateur.objects.filter(id=utilisateur_id)

    if utilisateurs_to_add:
        utilisateur.abonnements.add(utilisateurs_to_add[0])

    return redirect('home:home')