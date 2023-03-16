from django.http import HttpRequest, HttpResponseForbidden, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from esieeverse.models import Utilisateur
from publication.models import Choix

# Create your views here
class Abonnements(APIView):
    """
    Vue APIView pour gérer les abonnements de l'utilisateur
    """
    def post(self, request: HttpRequest) -> Response:
        """Ajoute un utilisateur aux abonnement d'un autre utilisateur

        Args:
            request (HttpRequest): La requête HTTP contenant l'id de l'utilisateur auquel on ajoutera un abonnement et l'id de l'utilisateur à ajouter

        Returns:
            Response: Réponse JSON
        """
        if request.COOKIES.get('csrfmiddlewaretoken', None) == None:
            return HttpResponseForbidden("Le token CSRF est manquant")

        id_utilisateur: int = request.POST.get('id_utilisateur')
        id_utilisateur_to_add: int = request.POST.get('id_utilisateur_to_add')

        try:
            utilisateur: Utilisateur = Utilisateur.objects.get(id=id_utilisateur)
            utilisateur_to_add: Utilisateur = Utilisateur.objects.get(id=id_utilisateur_to_add)
        except Utilisateur.DoesNotExist:
            return HttpResponseNotFound("L'utilisateur n'a pas été trouvé ! ")

        if utilisateur.abonnements.contains(utilisateur_to_add):
            return Response('Abonnement déjà ajouté')

        utilisateur.abonnements.add(utilisateur_to_add)
        utilisateur.save()

        return Response('Abonnement ajouté')
    
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
            utilisateur: Utilisateur = Utilisateur.objects.get(id=id_utilisateur)
            choix: Choix = Choix.objects.get(id=id_choix_to_select)
        except Utilisateur.DoesNotExist:
            return HttpResponseNotFound("L'utilisateur ou le choix n'a pas été trouvé !")
    
        if choix.utilisateurs.contains(utilisateur):
            return Response("L'utilisateur à déjà choisis ce choix")

        choix.utilisateurs.add(utilisateur)
        choix.save()

        return Response("Choix sélectionné")