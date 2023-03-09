from esieechat.models import Conversation, Message
from esieeverse.models import Utilisateur
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
class UtilisateurSerializer(serializers.HyperlinkedModelSerializer):
        user = UserSerializer()
        class Meta:
            model = Utilisateur
            fields = '__all__'