from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from publication.models import Publication

def home_view(request: HttpRequest) -> HttpResponse:
    # Récupère les publications selon les abonnements de l'utilisateur connecté
    publications = Publication.objects.filter(utilisateur__id__in=request.user.utilisateur.abonnements.all()).exclude(utilisateur_id=request.user.utilisateur)

    context = {
        'publications': publications,
    }

    return render(request,"home/index.html", context)
