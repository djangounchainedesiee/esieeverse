from django.shortcuts import render
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
from .models import Publication

# Create your views here.
def display(request: HttpRequest) -> HttpResponse:
    publications = Publication.objects.all().exclude(utilisateur_id=request.user.utilisateur)
    print(publications)

    context = {
        'publications': publications
    }
    
    return render(request, 'publication/displaypublications.html', context)