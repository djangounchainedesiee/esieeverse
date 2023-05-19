from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseForbidden
from django.db.models import Count
from rest_framework.response import Response
from publication.models import Publication, Evenement, Choix
from esieeverse.models import Utilisateur
from esieeverse.utils import check_utilisateur_auth
from publication.forms import CreatePublicationForm, CreateEvenementForm
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

    utilisateur: Utilisateur = request.user.utilisateur
    create_publication_form = CreatePublicationForm()
    create_evenement_form = CreateEvenementForm()

    """
    Enregistre un évènement si la requête POST contient toutes les informations. Sinon vérifie le contenu et enregistre une publication
    """
    if request.method == 'POST':

        # CREATE EVENEMENT
        create_evenement_form = CreateEvenementForm(request.POST, request.FILES)
        if create_evenement_form.is_valid():
            titre = create_evenement_form.cleaned_data['titre']
            contenu = create_evenement_form.cleaned_data['contenu']
            date_debut = create_evenement_form.cleaned_data['date_debut']
            date_fin = create_evenement_form.cleaned_data['date_fin']
            attached_file = create_evenement_form.cleaned_data['attachment']

            evenement = Evenement(titre=titre, contenu=contenu, date_debut=date_debut,
                                  date_fin=date_fin, attachment=attached_file, auteur=utilisateur)
            evenement.save()

            for nom_choix in request.POST.getlist('nom_choix', []):
                choix = Choix(nom=nom_choix, evenement=evenement)
                choix.save()

            create_evenement_form = CreateEvenementForm()
            return redirect('home:home_view')

        # CREATE PUBLICATION
        create_publication_form = CreatePublicationForm(request.POST, request.FILES)
        if create_publication_form.is_valid():
            titre = create_publication_form.cleaned_data['titre']
            contenu = create_publication_form.cleaned_data['contenu']

            attached_file = create_publication_form.cleaned_data['attachment']

            publication = Publication(
                titre=titre, contenu=contenu, attachment=attached_file, auteur=utilisateur)
            publication.save()
            return redirect('home:home_view')

    # MAJ des publications/evenements/abonnnées sur la home page
    publications = Publication.objects.filter(
        auteur_id__in=utilisateur.abonnements.all()).exclude(auteur_id=utilisateur)
    evenements = Evenement.objects.filter(
        auteur_id__in=utilisateur.abonnements.all()).exclude(auteur_id=utilisateur)
    abonnes = Utilisateur.objects.filter(abonnements=utilisateur)

    # Pour chaque choix on vérifie si l'utilisateur à déjà voté dessus
    for evenement in evenements:
        evenement.user_has_voted = Choix.objects.filter(
            evenement=evenement, utilisateurs=utilisateur).exists()

    # Aggrégat des publications avec likes et dislikes
    agregate_utilisateur_publications = Publication.objects.filter(
        auteur=utilisateur).aggregate(total_likes=Count('likes'), total_dislikes=Count('dislikes'))

    # Récup stats utilisateurs
    statistiques_utilisateur = {
        'nb_messages_envoye_utilisateur': request.user.utilisateur.message_set.all().count(),
        'total_likes': agregate_utilisateur_publications['total_likes'] or 0,
        'total_dislikes': agregate_utilisateur_publications['total_dislikes'] or 0
    }

    context = {
        'create_publication_form': create_publication_form,
        'create_evenement_form': create_evenement_form,
        'publications': publications,
        'evenements': evenements,
        'abonnes': abonnes,
        'statistiques_utilisateur': statistiques_utilisateur,
        'utilisateur': utilisateur
    }

    return render(request, "home/index.html", context)


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
        data={'id_utilisateur': utilisateur.id,
              'id_utilisateur_to_add': id_utilisateur},
        cookies={'csrfmiddlewaretoken': csrfmiddlewaretoken}
    )

    if response.status_code != 200:
        return HttpResponse(f"Erreur lors de l'appel à l'api", status=response.status_code)

    data = {
        'id_utilisateur_to_add': id_utilisateur,
    }

    return JsonResponse(data)


def voter(request: HttpRequest, id_choix: int) -> JsonResponse:
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

    utilisateur: Utilisateur = request.user.utilisateur

    response: Response = requests.post(
        f'http://127.0.0.1:8000/api/choixs/',
        data={'id_utilisateur': utilisateur.id,
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
