from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, JsonResponse, HttpResponseForbidden
from .models import Publication
from esieeverse.models import Utilisateur

# Create your views here.
def display(request: HttpRequest) -> HttpResponse:
    publications = Publication.objects.all().exclude(utilisateur_id=request.user.utilisateur)
    print(request.user.utilisateur.photo_de_profile)

    context = {
        'publications': publications
    }
    
    return render(request, 'publication/displaypublications.html', context)

def like(request: HttpRequest, id_publication: int) -> JsonResponse:
    if request.method != 'POST' or request.POST.get('csrfmiddlewaretoken', None) == None:
        return HttpResponseForbidden("Le token CSRF est manquant")

    publication = Publication.objects.get(id=id_publication)

    utilisateur: Utilisateur = request.user.utilisateur

    if publication.dislikes.contains(utilisateur):
            publication.dislikes.remove(utilisateur)

    if not publication.likes.contains(utilisateur):
        publication.likes.add(utilisateur)
        publication.save()

    data = {
        'id': id_publication,
        'nb_likes': publication.likes.count(),
        'nb_dislikes': publication.dislikes.count(),
    }

    return JsonResponse(data)
        
def dislike(request: HttpRequest, id_publication: int) -> JsonResponse:
    if request.method != 'POST' or request.POST.get('csrfmiddlewaretoken', None) == None:
        return HttpResponseForbidden("Le token CSRF est manquant")

    publication = Publication.objects.get(id=id_publication)

    utilisateur: Utilisateur = request.user.utilisateur

    if publication.likes.contains(utilisateur):
            publication.likes.remove(utilisateur)

    if not publication.dislikes.contains(utilisateur):
        publication.dislikes.add(utilisateur)
        publication.save()

    data = {
        'id': id_publication,
        'nb_likes': publication.likes.count(),
        'nb_dislikes': publication.dislikes.count(),
    }
    print('Dislike data : ', data)

    return JsonResponse(data)