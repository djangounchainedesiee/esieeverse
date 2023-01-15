from channels.generic.websocket import AsyncWebsocketConsumer
import json
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    """
    Classe héritiaire de AsyncWebsocketConsumer permettant de gérer la réception et l'envoi des messages sur les différents channels websockets
    """
    async def connect(self):
        # Etablie une connexion avec le websocket
        self.conversation_id = self.scope['url_route']['kwargs']['conversation_id']
        self.conversation_group_name = 'chat_%s' % self.conversation_id
        print('Connect to groupName : ', self.conversation_id)
        await self.channel_layer.group_add(
            self.conversation_id,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Est appelé lorsque la connexion avec le websocket est fermé
        await self.channel_layer.group_discard(
            self.conversation_id,
            self.channel_name
        )

    async def receive(self, text_data):
        print('Receive Message : ', text_data)
        # Est appelé lorsqu'un client websocket connecté nous envoie un message, l'objet reçu est envoyé à tous les autres clients connectés
        message_json = json.loads(text_data)
        contenu = message_json['contenu']
        conversation_id = message_json['conversation_id']
        id_utilisateur = message_json['utilisateur']['id']
        nom_utilisateur = message_json['utilisateur']['nom']
        date_heure = message_json['date_heure']

        await self.channel_layer.group_send(
            self.conversation_id, {
                'type': 'send_message',
                'contenu': contenu,
                'conversation_id': conversation_id,
                'utilisateur': {
                    'id': id_utilisateur,
                    'nom': nom_utilisateur,
                },
                'date_heure': date_heure
        })

    async def send_message(self, event):
        print('Send Message : ', event)
        # Est appelé lorsqu'un autre client websocket (exemple receive) nous envoi un message on lui répond alors à son message
        contenu = event['contenu']
        conversation_id = event['conversation_id']
        id_utilisateur = event['utilisateur']['id']
        nom_utilisateur = event['utilisateur']['nom']
        date_heure = event['date_heure']

        await self.send(text_data=json.dumps({
                'contenu': contenu,
                'conversation_id': conversation_id,
                'utilisateur': {
                    'id': id_utilisateur,
                    'nom': nom_utilisateur,
                },
                'date_heure': date_heure
        }))
