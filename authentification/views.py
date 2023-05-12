from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from esieeverse.models import Filiere, Utilisateur, Promotion

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            raw_password = form.cleaned_data.get('password1')
            user.set_password(raw_password)
            user.save()
            login(request, user)
            messages.success(request, f'Hello {user.username}, Your account has been created successfully!')

            filiere_app_nom = form.cleaned_data.get('ma_filliere_app')
            cursus_nom = form.cleaned_data.get('cursus')

            if cursus_nom == 'apprentissage':
                filiere_nom = form.cleaned_data.get('ma_filliere_app')
            else:
                filiere_nom = form.cleaned_data.get('ma_filliere_tp')

            promotion_nom = form.cleaned_data.get('ma_promotion')

            utilisateur = Utilisateur(filiere=Filiere.objects.get(nom=filiere_nom),
                                      promotion=Promotion.objects.get(nom=promotion_nom),
                                      photo_de_profile=form.cleaned_data.get('profile_picture'))
            utilisateur.save()

            return redirect('accounts')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})
