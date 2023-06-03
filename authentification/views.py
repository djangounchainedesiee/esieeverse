from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from esieeverse.models import Filiere, Utilisateur, Promotion
from django.contrib.auth.models import User

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():
            # Créer un nouvel utilisateur
            user = User.objects.create_user(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )

            # Ajouter les autres données d'inscription à l'utilisateur
            user.first_name = form.cleaned_data['Prénom']
            user.last_name = form.cleaned_data['Nom']
            user.profile_picture = form.cleaned_data['profile_picture']
            user.ma_promotion = form.cleaned_data['ma_promotion']
            user.cursus = form.cleaned_data['cursus']
            user.ma_filliere_app = form.cleaned_data['ma_filliere_app']
            user.ma_filliere_tp = form.cleaned_data['ma_filliere_tp']
            user.entreprise = form.cleaned_data['entreprise']
            user.save()

            # Rediriger vers la page de connexion
            return redirect('home:home_view')
    else:
        form = SignUpForm()
    return render(request, 'authentification/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'authentification/login.html'
    form_class = AuthenticationForm
    

def logout_view(request):
    logout(request)
    return redirect('login/')
