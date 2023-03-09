from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_protect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from esieeverse.models import Utilisateur
from .serializers import UtilisateurSerializer

# Create your views here


class Abonnements(APIView):
    @csrf_protect
    def post(self, request: HttpRequest):
        id_utilisateur = request.POST.get('id_utilisateur')
        id_utilisateur_to_add = request.POST.get('id_utilisateur_to_add')

        try:
            utilisateur = Utilisateur.objects.get(id=id_utilisateur)
            utilisateur_to_add = Utilisateur.objects.get(id=id_utilisateur_to_add)
        except Utilisateur.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        utilisateur.abonnements.add(utilisateur_to_add)
        utilisateur.save()
        serializer = UtilisateurSerializer(utilisateur)

        return Response(serializer.data)
