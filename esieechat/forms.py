from django import forms
from django.contrib.auth.models import User, Permission

UTILISATEUR_CHOICES = User.objects.filter(groups__name='etudiants').distinct()

class ConversationUtilisateursForm(forms.Form):
        nomConversation = forms.CharField(label='Nom de la conversation', max_length=20)
        utilisateurs = forms.ChoiceField(label='Choisissez des utilisateurs', choices=UTILISATEUR_CHOICES)