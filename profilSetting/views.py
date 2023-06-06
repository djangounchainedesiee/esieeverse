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
    setting_form = SettingForm()

    if request.method == "POST":
        setting_form = SettingForm(request.POST, request.FILES)

        if setting_form.is_valid():
            password = setting_form.cleaned_data['password']
            photo_de_profile = setting_form.cleaned_data['photo_de_profile']
            first_name = setting_form.cleaned_data['first_name']
            last_name = setting_form.cleaned_data['last_name']
            login = setting_form.cleaned_data['login']
            email = setting_form.cleaned_data['email']

            if password is not None and len(password) > 0:
                utilisateur.user.set_password(password) 

            if first_name is not None and len(first_name) > 0:
                utilisateur.user.first_name = first_name 

            if last_name is not None and len(last_name) > 0:
                utilisateur.user.last_name = last_name 

            if login is not None and len(login) > 0:
                utilisateur.user.username = login 

            if email is not None and len(email) > 0:
                utilisateur.user.email = email 
                    
            if photo_de_profile is not None:
                utilisateur.photo_de_profile = photo_de_profile
            
            utilisateur.user.save()
            utilisateur.save()

            return redirect("profil:view_profil", id_utilisateur = utilisateur.id)
        
    context = {
        "setting_form": setting_form,
        "utilisateur": utilisateur,
    }

    return render(request, 'profilSetting/profilSetting.html',  context)


