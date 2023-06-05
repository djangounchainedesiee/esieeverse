from django.shortcuts import render, redirect,get_object_or_404
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
                first_name=form.cleaned_data['Prénom'],
                last_name = form.cleaned_data['Nom'],
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )


            # Ajouter les autres données d'inscription à l'utilisateur


            cursus = form.cleaned_data['cursus']

            if(cursus=="apprentissage"):
                filiere_nom = form.cleaned_data['ma_filliere_app']

            if(cursus=="temps plein"):
                filiere_nom = form.cleaned_data['ma_filliere_tp']


            filiere = get_object_or_404(Filiere, nom=filiere_nom)  
            #si mon cursus est app alors filliere-> ma filiere app
            

            promotion_id = form.cleaned_data['ma_promotion']
            promotion = get_object_or_404(Promotion, nom=promotion_id)  # Récupérer l'instance de Promotion correspondante


            utilisateur = Utilisateur.objects.create(
                prenom = form.cleaned_data['Prénom'],
                nom = form.cleaned_data['Nom'],
                user=user,
                promotion= promotion,
                filiere=filiere,
                photo_de_profile=form.cleaned_data['profile_picture'],
                entreprise=form.cleaned_data['entreprise']
            )


            utilisateur.save()

            user.save()

            # Rediriger vers la page de connexion
            return redirect('home:home_view')
    else:
        form = SignUpForm()
    return render(request, 'Registration/signup.html', {'form': form})


class CustomLoginView(LoginView):
    template_name = 'Registration/login.html'
    form_class = AuthenticationForm
    

def logout_view(request):
    logout(request)
    return redirect('login/')
