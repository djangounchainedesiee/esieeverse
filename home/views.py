from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseForbidden, HttpResponseBadRequest
from rest_framework.response import Response
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
    abonnes = Utilisateur.objects.filter(abonnements=request.user.utilisateur)

    context = {
        'publications': publications,
        'abonnes': abonnes
    }

    return render(request,"home/index.html", context)

def add_friend(request: HttpRequest, id_utilisateur: int) -> JsonResponse:
    """Ajoute un ami à l'utilisateur

    Args:
        request (HttpRequest): La requête
        id_utilisateur (int): L'id de l'utilisateur à ajouter

    Returns:
        HttpResponse: Redirige vers la vue principale
    """
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken', None)
    if request.method != 'POST' or request.POST.get('csrfmiddlewaretoken', None) == None:
        return HttpResponseForbidden("Le token CSRF est manquant")

    utilisateur: Utilisateur = request.user.utilisateur
    
    response: Response = requests.post( 
        reverse('api:abonnement'), 
        data={'id_utilisateur': utilisateur.id, 'id_utilisateur_to_add': id_utilisateur}, 
        cookies={'csrftoken': csrfmiddlewaretoken}
    )

    if response.status_code != 200:
        return HttpResponseBadRequest(f"Erreur lors de l'appel à l'api. Code {response.status_code} : {response.status_text}")
    
    data = {
        'id_utilisateur_to_add': id_utilisateur,
    }

    return JsonResponse(data)