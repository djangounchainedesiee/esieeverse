from django import forms
from esieeverse.models import Utilisateur
from django.contrib.auth.models import User
from .models import Message
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Row, Column)

class ConversationUtilisateursForm(forms.Form):
    """
    Représente un fomulaire perttant de créer une conversation en choisisant ses utilisations et son nom
    """
    def __init__(self, *args, **kwargs):
        utilisateur_connecte = kwargs.pop('utilisateur_connecte')
        super().__init__(*args, **kwargs)
        self.fields['utilisateurs'].queryset = Utilisateur.objects.all().exclude(id=utilisateur_connecte.id)

    nom_conversation = forms.CharField(label='Nom de la conversation', max_length=20)
    utilisateurs = forms.ModelMultipleChoiceField(label='Choisissez des utilisateurs', queryset=Utilisateur.objects.none())

class MessageForm(forms.ModelForm):
    """
    Représente un fomulaire perttant d'envoyer un message
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'POST'
        self.helper.layout = Layout(
            Row(Column('contenu', css_class='form-control')),
        )
        self.fields['contenu'].widget.attrs = {'rows': 2}

    class Meta:
        model = Message
        fields = ['contenu']


class ConversationAddUtilisateurForm(forms.Form):
    """
    Représente un fomulaire perttant d'ajouter un utilisateur à la conversation
    """
    def __init__(self, conversation_id, *args,**kwargs):
        self.conversation_id = conversation_id
        super().__init__(*args, **kwargs)
        self.fields['utilisateurs'] = forms.ModelMultipleChoiceField(
            label='Choisissez des utilisateurs', 
            queryset=Utilisateur.objects.filter(user__in=User.objects.filter(groups__name='etudiants')).exclude(conversation__id=self.conversation_id)
        )