from esieechat.models import Conversation, Message
from esieeverse.models import Utilisateur
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'username', 'last_name', 'first_name']

class UtilisateurSerializer(serializers.HyperlinkedModelSerializer):
        user = UserSerializer()
        class Meta:
            model = Utilisateur
            fields = ['id', 'user']

class ConversationsSerizalizer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'nom']

class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='conversation-detail',source='profile',)
    conversation =  ConversationsSerizalizer()
    utilisateur = UtilisateurSerializer()

    class Meta:
        model = Message
        fields = ['id', 'contenu', 'date_heure', 'conversation', 'utilisateur']