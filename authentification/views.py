from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from esieeverse.models import Filiere, Utilisateur, Promotion

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST, request.FILES)
        if form.is_valid():

            #user = form.save(commit=False)
            #user.profile_picture = form.cleaned_data.get('profile_picture')
            #user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            messages.success(request, f'Hello {user.username}, Your account has been created successfully!')



            filiere_app_nom =form.cleaned_data.get('ma_filliere_app')
            cursus_nom=form.cleaned_data.get('cursus')

            if cursus_nom =='apprentissage':
                filiere_nom=form.cleaned_data.get('ma_filliere_app')
            else :
                filiere_nom=form.cleaned_data.get('ma_filliere_tp')
            


            promotion_nom = form.cleaned_data.get('ma_promotion')


            utilisateur=Utilisateur(filiere=Filiere.objects.get(nom=filiere_nom),
                                    promotion=Promotion.objects.get(nom=promotion_nom),
                                    photo_de_profile = form.cleaned_data.get('profile_picture'))
            
            
            utilisateur.save()

            return redirect('accounts')
    else:
        form = SignUpForm()
    return render(request, 'registration/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if 'next' in request.GET:
                return redirect(request.GET['next'])
            else:
                return redirect('home')
        else:
            error_message = 'Nom d\'utilisateur ou mot de passe incorrect'
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')
    

def logout_view(request):
    logout(request)
    return redirect('login/')