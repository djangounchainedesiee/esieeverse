from django.http import HttpRequest, HttpResponse, HttpResponseForbidden, HttpResponseNotFound
from rest_framework.response import Response
from rest_framework.views import APIView
from esieeverse.models import Utilisateur

# Create your views here
class Abonnements(APIView):
    def post(self, request: HttpRequest) -> HttpResponse:
        if request.COOKIES.get('csrfmiddlewaretoken', None) == None:
            return HttpResponseForbidden("Le token CSRF est manquant")

        id_utilisateur = request.POST.get('id_utilisateur')
        id_utilisateur_to_add = request.POST.get('id_utilisateur_to_add')

        try:
            utilisateur = Utilisateur.objects.get(id=id_utilisateur)
            utilisateur_to_add = Utilisateur.objects.get(id=id_utilisateur_to_add)
        except Utilisateur.DoesNotExist:
            return HttpResponseNotFound("L'utilisateur n'a pas été trouvé ! ")

        if utilisateur.abonnements.contains(utilisateur_to_add):
            return Response('Abonnement déjà ajouté')

        utilisateur.abonnements.add(utilisateur_to_add)
        utilisateur.save()

        return Response('Abonnement ajouté')