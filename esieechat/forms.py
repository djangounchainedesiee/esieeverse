from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Row, Column)
from esieeverse.models import Utilisateur
from .models import Message, Conversation

class CreateConversationUtilisateursForm(forms.Form):
    """
    Représente un fomulaire perttant de créer une conversation en choisisant ses utilisations et son nom
    """
    def __init__(self, *args, **kwargs):
        utilisateur_connecte = kwargs.pop('utilisateur_connecte')
        super().__init__(*args, **kwargs)
        self.fields['utilisateurs'].queryset = Utilisateur.objects.all().exclude(id=utilisateur_connecte.id)

    nom_conversation = forms.CharField(label='Nom de la conversation', max_length=20)
    utilisateurs = forms.ModelMultipleChoiceField(label='Choisissez des utilisateurs', queryset=Utilisateur.objects.none())

class EditConversationUtilisateursForm(forms.Form):
    """
    Représente un fomulaire perttant de créer une conversation en choisisant ses utilisations et son nom
    """
    def __init__(self, *args, **kwargs):
        id_conversation = kwargs.pop('id_conversation')
        utilisateur_connecte = kwargs.pop('utilisateur_connecte')
        super().__init__(*args, **kwargs)
        conversation: Conversation = Conversation.objects.get(id=id_conversation) 
        self.fields['utilisateurs'].queryset = Utilisateur.objects.all().exclude(id=utilisateur_connecte.id)
        self.fields['nom_conversation'].initial = conversation.nom

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
    def __init__(self, *args,**kwargs):
        self.id_conversation = kwargs.pop('id_conversation')
        super().__init__(*args, **kwargs)
        self.fields['utilisateurs'] = forms.ModelMultipleChoiceField(
            label='Choisissez des utilisateurs', 
            queryset=Utilisateur.objects.all().exclude(conversation_id=self.id_conversation)
        )