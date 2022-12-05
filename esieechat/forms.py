from django import forms
from esieeverse.models import Utilisateur
from django.contrib.auth.models import User
from .models import Message
from crispy_forms.helper import FormHelper
from crispy_forms.layout import (Layout, Row, Column)


class ConversationUtilisateursForm(forms.Form):
    nom_conversation = forms.CharField(
        label='Nom de la conversation', max_length=20)
    utilisateurs = forms.ModelMultipleChoiceField(
        label='Choisissez des utilisateurs', queryset=Utilisateur.objects.filter(user_id__in=User.objects.filter(groups__name='etudiants').values('id')))


class MessageForm(forms.ModelForm):
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
