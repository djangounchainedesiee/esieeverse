from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def profil_setting(request: HttpRequest) -> HttpResponse:
        return render(request, 'profilSetting/profilSetting.html')
