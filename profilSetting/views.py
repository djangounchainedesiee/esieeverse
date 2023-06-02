from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpRequest
from .forms import SettingForm
from esieeverse.models import Utilisateur
from esieeverse.utils import check_utilisateur_auth
import os

# Create your views here.
def profil_setting(request: HttpRequest) -> HttpResponse:
    if not check_utilisateur_auth(request):
        return redirect('auth:login')

    utilisateur: Utilisateur = request.user.utilisateur
    form = SettingForm()

    if request.method == "POST":
        form = SettingForm(request.POST,request.FILES)

        if form.is_valid():
            password = form.cleaned_data['password']
            photo_Profile = form.cleaned_data['PhotoProfile']
            print(photo_Profile)

            utilisateur.user.set_password(password) 
            utilisateur.photo_de_profile = photo_Profile
            utilisateur.save()
            return redirect("profil:view_profil", id_utilisateur = utilisateur.id)

    return render(request, 'profilSetting/profilSetting.html',  {"form": form})


