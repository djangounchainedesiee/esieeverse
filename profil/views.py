from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseForbidden
from django.db.models import Count
from rest_framework.response import Response
from esieeverse.utils import check_utilisateur_auth
from esieeverse.models import Utilisateur
from publication.models import Publication, Evenement, Choix
import requests

# Create your views here.


def view_profil(request: HttpRequest, id_utilisateur: int) -> HttpResponse:
    if not check_utilisateur_auth(request):
        return redirect('auth:login')

    utilisateur: Utilisateur = Utilisateur.objects.get(id=id_utilisateur)

    # MAJ des publications/evenements/abonnnées sur la home page
    publications = Publication.objects.filter(auteur=utilisateur).order_by('-date')
    evenements = Evenement.objects.filter(auteur=utilisateur).order_by('-date_debut')
    abonnes = Utilisateur.objects.filter(abonnements=utilisateur)

    # Pour chaque choix on vérifie si l'utilisateur à déjà voté dessus
    for evenement in evenements:
        evenement.user_has_voted = Choix.objects.filter(
            evenement=evenement, utilisateurs=utilisateur).exists()

    # Aggrégat des publications avec likes et dislikes
    agregate_utilisateur_publications = Publication.objects.filter(
        auteur=utilisateur).aggregate(total_likes=Count('likes'), total_dislikes=Count('dislikes'))

    statistiques_utilisateur = {
        'nb_messages_envoye_utilisateur': utilisateur.message_set.all().count(),
        'total_likes': agregate_utilisateur_publications['total_likes'] or 0,
        'total_dislikes': agregate_utilisateur_publications['total_dislikes'] or 0
    }

    context = {
        'utilisateur': utilisateur,
        'publications': publications,
        'evenements': evenements,
        'abonnes': abonnes,
        'abonnements': utilisateur.abonnements.all(),
        'statistiques_utilisateur': statistiques_utilisateur,
    }

    return render(request, "profil/index.html", context)


def add_friend(request: HttpRequest, id_utilisateur: int) -> JsonResponse:
    """Ajoute un ami à l'utilisateur

    Args:
        request (HttpRequest): La requête
        id_utilisateur (int): L'id de l'utilisateur de la page

    Returns:
        HttpResponse: Redirige vers la page principal
    """
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken', None)
    if request.method != 'POST' or csrfmiddlewaretoken == None:
        return HttpResponseForbidden("Le token CSRF est manquant")

    utilisateur_connecte: Utilisateur = request.user.utilisateur

    response: Response = requests.post(
        f'http://127.0.0.1:8000/api/abonnements/',
        data={'id_utilisateur': utilisateur_connecte.id,
              'id_utilisateur_to_add': id_utilisateur},
        cookies={'csrfmiddlewaretoken': csrfmiddlewaretoken}
    )

    if response.status_code != 200:
        return HttpResponse(f"Erreur lors de l'appel à l'api", status=response.status_code)

    data = {
        'id_utilisateur_to_add': id_utilisateur,
    }

    return JsonResponse(data)


def voter(request: HttpRequest, id_utilisateur: int, id_choix: int) -> JsonResponse:
    """Ajoute un ami à l'utilisateur

    Args:
        request (HttpRequest): La requête
        id_choix (int): L'id du choix auquel voter

    Returns:
        HttpResponse: Redirige vers la page principal
    """
    csrfmiddlewaretoken = request.POST.get('csrfmiddlewaretoken', None)
    if request.method != 'POST' or csrfmiddlewaretoken == None:
        return HttpResponseForbidden("Le token CSRF est manquant")

    utilisateur_connecte: Utilisateur = request.user.utilisateur

    response: Response = requests.post(
        f'http://127.0.0.1:8000/api/choixs/',
        data={'id_utilisateur': utilisateur_connecte.id,
              'id_choix_to_select': id_choix},
        cookies={'csrfmiddlewaretoken': csrfmiddlewaretoken}
    )

    if response.status_code != 200:
        return HttpResponse(f"Erreur lors de l'appel à l'api choixs", status=response.status_code)

    evenement: Evenement = Choix.objects.get(id=id_choix).evenement

    response = requests.get(
        f'http://127.0.0.1:8000/api/evenements/{evenement.id}/choixs/')

    if response.status_code != 200:
        return HttpResponse(f"Erreur lors de l'appel à l'api evenement pour récupérer ses choix ", status=response.status_code)

    response_json: dict = response.json()

    data = {
        'choixs': response_json['choixs_evenement'],
        'total_votes': response_json['total_votes'],
    }

    return JsonResponse(data)
