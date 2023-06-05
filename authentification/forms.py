from django import forms
from django.contrib.auth.forms import UserCreationForm
from esieeverse.models import Filiere

class SignUpForm(forms.Form):


    

    #champs d'auth

    username = forms.CharField(max_length=150, label='Nom d\'utilisateur')

    email = forms.EmailField(max_length=254, help_text = 'Entrez une adresse mail ESIEE.')
    
    password = forms.CharField(widget=forms.PasswordInput(), label='Mot de passe')
    password_confirm = forms.CharField(widget=forms.PasswordInput, label='Confirmation du mot de passe')

    def clean_password_confirm(self):
        password = self.cleaned_data.get("password")
        password_confirm = self.cleaned_data.get("password_confirm")
        if password and password_confirm and password != password_confirm:
            raise forms.ValidationError("Les mots de passe ne correspondent pas.")
        return password_confirm
    
    #
    
    #champs information utilisateur

    profile_picture = forms.ImageField(required=False, widget=forms.ClearableFileInput(),  label='Photo du profil')

    Prénom = forms.CharField(label='Prénom', max_length=150)

    Nom = forms.CharField(label='Nom', max_length=150)

    CHOICES = [('E1','E1'),('E2','E2'),('E3','E3'),('E4','E4'),('E5','E5') ]
    ma_promotion= forms.ChoiceField(choices=CHOICES, initial='1')

    Cursus_Type = (
        ('apprentissage', 'Apprentissage'),
        ('temps plein', 'Temps Plein'),
    )   
    cursus = forms.ChoiceField(widget=forms.RadioSelect, choices=Cursus_Type)

    CHOICES_app = [('FR','Réseaux et sécurité'),('FE','Systèmes embarqués'),('FI','Informatique et applications'),('FG','Génie industriel'),('FT','Energies') ]
    ma_filliere_app= forms.ChoiceField(choices=CHOICES_app, initial='1')

    CHOICES_tp = [('INF','Informatique'),('CYB','Cybersécurité'),('DSIA','Datascience et intelligence artificielle'),('AIC','Artificial intelligence and cybersecurity'),('SE','Systèmes embarqués'), ('SEI','Systèmes électroniques intelligents'),('GI','Génie industriel'),('BIO','Biotechnologies et e-Santé'),('ENE','Energie')]
    ma_filliere_tp= forms.ChoiceField(choices=CHOICES_tp, initial='1')

    


    entreprise = forms.CharField(max_length=100,  required=False, label="Nom de l'entreprise")
  
    #