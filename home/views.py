from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponse, HttpResponseForbidden
from django.db.models.query import QuerySet
from rest_framework.response import Response
from publication.models import Publication, Evenement, Choix
from esieeverse.models import Utilisateur
from esieeverse.utils import check_utilisateur_auth
from typing import List
import requests

def home_view(request: HttpRequest) -> HttpResponse:
    """Génère la vue principale contenant le flux d'actualité de la personne

    Args:
        request (HttpRequest): La requête

    Returns:
        HttpResponse: Affiche la vue de la page principale
    """
    if not check_utilisateur_auth(request):
        return redirect('auth:login')

    publications = Publication.objects.filter(auteur_id__in=request.user.utilisateur.abonnements.all()).exclude(auteur_id=request.user.utilisateur)
    evenements = Evenement.objects.filter(auteur_id__in=request.user.utilisateur.abonnements.all()).exclude(auteur_id=request.user.utilisateur)
    abonnes = Utilisateur.objects.filter(abonnements=request.user.utilisateur)

    context = {
        'publications': publications,
        'evenements': evenements,
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
    if request.method != 'POST' or csrfmiddlewaretoken == None:
        return HttpResponseForbidden("Le token CSRF est manquant")

    utilisateur: Utilisateur = request.user.utilisateur
    
    response: Response = requests.post( 
        f'http://127.0.0.1:8000/api/abonnements/', 
        data={'id_utilisateur': utilisateur.id, 'id_utilisateur_to_add': id_utilisateur}, 
        cookies={'csrfmiddlewaretoken': csrfmiddlewaretoken}
    )

    if response.status_code != 200:
        return HttpResponse(f"Erreur lors de l'appel à l'api", status=response.status_code)

    data = {
        'id_utilisateur_to_add': id_utilisateur,
    }

    return JsonResponse(data)

def voter(request: HttpRequest, id_choix: int):
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken', None)
    if request.method != 'POST' or csrfmiddlewaretoken == None:
        return HttpResponseForbidden("Le token CSRF est manquant")
    
    utilisateur: Utilisateur = request.user.utilisateur

    response: Response = requests.post( 
        f'http://127.0.0.1:8000/api/choixs/', 
        data={'id_utilisateur': utilisateur.id, 'id_choix_to_select': id_choix}, 
        cookies={'csrfmiddlewaretoken': csrfmiddlewaretoken}
    )

    if response.status_code != 200:
        return HttpResponse(f"Erreur lors de l'appel à l'api", status=response.status_code)
    
    evenement: Evenement = Choix.objects.get(id=id_choix).evenement
    choixs_evenement: List[Choix] = list(evenement.choix_set.all().values())

    data = {
        'choixs': choixs_evenement,
        'id_choix': id_choix
    }

    return JsonResponse(data)