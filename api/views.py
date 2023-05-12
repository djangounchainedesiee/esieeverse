from django.http import HttpRequest, HttpResponseForbidden, HttpResponseNotFound
from django.db.models import Count
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from typing import Dict, List, Union
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from esieeverse.models import Utilisateur
from publication.models import Choix, Evenement

# Create your views here


class Abonnements(APIView):
    """
    Vue APIView pour gérer les abonnements de l'utilisateur
    """

    def post(self, request: HttpRequest) -> Response:
        """Ajoute ou supprime un utilisateur aux abonnement d'un autre utilisateur

        Args:
            request (HttpRequest): La requête HTTP contenant l'id de l'utilisateur auquel on ajoutera ou supprimera un abonnement et l'id de l'utilisateur à ajouter

        Returns:
            Response: Réponse JSON
        """
        if request.COOKIES.get('csrfmiddlewaretoken', None) == None:
            return HttpResponseForbidden("Le token CSRF est manquant")

        id_utilisateur: int = request.POST.get('id_utilisateur')
        id_utilisateur_to_add: int = request.POST.get('id_utilisateur_to_add')

        try:
            utilisateur: Utilisateur = Utilisateur.objects.get(
                id=id_utilisateur)
            utilisateur_to_add: Utilisateur = Utilisateur.objects.get(
                id=id_utilisateur_to_add)
        except Utilisateur.DoesNotExist:
            return HttpResponseNotFound("L'utilisateur n'a pas été trouvé ! ")
                
        if utilisateur.abonnements.contains(utilisateur_to_add):
            utilisateur.abonnements.remove(utilisateur_to_add)
        else:
            if utilisateur.banis.contains(utilisateur_to_add) or utilisateur_to_add.banis.contains(utilisateur):
                return HttpResponseForbidden("L'utilisateur est bannis !")
            
            utilisateur.abonnements.add(utilisateur_to_add)

        utilisateur.save()

        return Response('Abonnement ajouté')


class Banis(APIView):
    """
    Vue APIView pour gérer les banis de l'utilisateur
    """

    def post(self, request: HttpRequest) -> Response:
        """Ajoute / Supprime un utilisateur aux banis d'un autre utilisateur

        Args:
            request (HttpRequest): La requête HTTP contenant l'id de l'utilisateur auquel on ajoutera ou supprimera un banis et l'id de l'utilisateur à ajouter

        Returns:
            Response: Réponse JSON
        """
        if request.COOKIES.get('csrfmiddlewaretoken', None) == None:
            return HttpResponseForbidden("Le token CSRF est manquant")

        id_utilisateur: int = request.POST.get('id_utilisateur')
        id_utilisateur_to_add: int = request.POST.get('id_utilisateur_to_add')

        try:
            utilisateur: Utilisateur = Utilisateur.objects.get(
                id=id_utilisateur)
            utilisateur_to_add: Utilisateur = Utilisateur.objects.get(
                id=id_utilisateur_to_add)
        except Utilisateur.DoesNotExist:
            return HttpResponseNotFound("L'utilisateur n'a pas été trouvé ! ")

        if utilisateur.banis.contains(utilisateur_to_add):
            utilisateur.banis.remove(utilisateur_to_add)
        else:
            utilisateur.banis.add(utilisateur_to_add)
            
            if utilisateur.abonnements.contains(utilisateur_to_add):
                utilisateur.abonnements.remove(utilisateur_to_add)
        
        utilisateur.save()

        return Response('Banis modifié')

class Choixs(APIView):
    """
    Vue APIView pour gérer les choix d'un évènement et d'un utilisateur
    """

    def post(self, request: HttpRequest) -> Response:
        """Selectionne un choix pour un utilisateur

        Args:
            request (HttpRequest): La requête HTTP contenant l'id de l'utilisateur auquel on sélectionnera un choix et l'id du choix à sélectionner

        Returns:
            Response: Réponse JSON
        """
        if request.COOKIES.get('csrfmiddlewaretoken', None) == None:
            return HttpResponseForbidden("Le token CSRF est manquant")

        id_utilisateur: int = request.POST.get('id_utilisateur')
        id_choix_to_select: int = request.POST.get('id_choix_to_select')

        try:
            utilisateur: Utilisateur = Utilisateur.objects.get(
                id=id_utilisateur)
            choix: Choix = Choix.objects.get(id=id_choix_to_select)
        except Utilisateur.DoesNotExist:
            return HttpResponseNotFound("L'utilisateur ou le choix n'a pas été trouvé !")

        if choix.utilisateurs.contains(utilisateur):
            return Response("L'utilisateur à déjà choisis ce choix")

        choix.utilisateurs.add(utilisateur)
        choix.save()

        return Response("Choix sélectionné")


@api_view(['GET'])
def getAllChoixsWithTotalVotesByEvenement(request: HttpRequest, id_evenement: int) -> JsonResponse:
    """Récupère tous les choix d'un évènement avec le nombre de votes total de votes

    Args:
        request (HttpRequest): La requête
        id_evenement (int): L'évènement où il faut récupérer les choix

    Returns:
        JsonResponse: Réponse JSON sur les choix d'un évènement avec le nombre de votes total de votes
    """
    try:
        evenement: Evenement = Evenement.objects.get(id=id_evenement)
    except Evenement.DoesNotExist:
        return HttpResponseNotFound(f"L'événement avec l'identifiant {id_evenement} n'a pas été trouvé !")

    choixs_evenement = evenement.choix_set.all()
    total_votes = evenement.total_votes()

    choixs_evenement = [
        {
            'id': choix.id,
            'nom': choix.nom,
            'nb_votes': choix.nb_utilisateurs(),
            'pourcentage': choix.pourcentage()
        }
        for choix in choixs_evenement
    ]

    response_data = {
        'total_votes': total_votes,
        'choixs_evenement': choixs_evenement
    }

    return JsonResponse(response_data)
