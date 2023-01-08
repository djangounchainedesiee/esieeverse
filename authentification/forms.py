from django import forms
from django.contrib.auth.forms import UserCreationForm
from esieeverse.models import Utilisateur
from esieeverse.models import Promotion
from esieeverse.models import Classe
from esieeverse.models import Fillière


class SignUpForm(forms.Form):

    email = forms.EmailField(max_length=254, help_text = 'Requis. Entrez une adresse mail valide.')

    Nom = forms.CharField(
        label='Nom de famille de l\'utilisateur', max_length=150)

    Prénom = forms.CharField(
        label='Prénom de l\'utilisateur', max_length=150)

    

    password = forms.CharField(widget=forms.PasswordInput())

