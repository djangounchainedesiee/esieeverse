from django import forms
from django.contrib.auth.forms import UserCreationForm
class SignUpForm(forms.Form):

    Prénom = forms.CharField(label='Prénom', max_length=150)

    Nom = forms.CharField(label='Nom ', max_length=150)

    email = forms.EmailField(max_length=254, help_text = 'Requis. Entrez une adresse mail valide.')

    password = forms.CharField(widget=forms.PasswordInput())

    CHOICES = [('1','E1'),('2','E2'),('3','E3'),('4','E4'),('5','E5') ]
    ma_promotion= forms.ChoiceField(choices=CHOICES)

    
 
