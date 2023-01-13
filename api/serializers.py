from esieechat.models import Conversation, Message
from rest_framework import serializers

class ConversationsSerizalize(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Conversation
        fields = ['id', 'nom']

class MessagesSerializer(serializers.HyperlinkedModelSerializer):
    #url = serializers.HyperlinkedIdentityField(view_name='conversation-detail',source='profile',)
    conversation =  ConversationsSerizalize()

    class Meta:
        model = Message
        fields = ['id', 'contenu', 'date_heure', 'conversation']