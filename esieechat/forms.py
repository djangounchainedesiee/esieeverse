from django import forms
from django.contrib.auth.models import User, Permission
class ConversationUtilisateursForm(forms.Form):
        nomConversation = forms.CharField(label='Nom de la conversation', max_length=20)
        utilisateurs = forms.ModelChoiceField(label='Choisissez des utilisateurs', queryset=User.objects.filter(groups__name='etudiants'))