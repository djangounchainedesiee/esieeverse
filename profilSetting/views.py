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

            print('password : ', password)

            if password is not None and len(password) > 0:
                print('Changement mot de passe verif : ', utilisateur.user.check_password(str(password)))
                if utilisateur.user.check_password(str(password)): 
                    print('Changement mot de passe')
                    utilisateur.user.set_password(password) 
                else:
                    context = {
                        "setting_form": setting_form,
                        "utilisateur": utilisateur,
                        "error": "Votre nouveau mot de passe est similaire au précédant ou il n'est pas assez fort"
                    }

                    return render(request, 'profilSetting/profilSetting.html',  context)
                    
            if photo_de_profile is not None:
                utilisateur.photo_de_profile = photo_de_profile

            utilisateur.save()

            return redirect("profil:view_profil", id_utilisateur = utilisateur.id)
        
    context = {
        "setting_form": setting_form,
        "utilisateur": utilisateur,
    }

    return render(request, 'profilSetting/profilSetting.html',  context)


