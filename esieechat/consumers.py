from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from django.utils import dateformat
import json
from .models import Message


class ChatConsumer(AsyncWebsocketConsumer):
    """
    Classe héritiaire de AsyncWebsocketConsumer permettant de gérer la réception et l'envoi des messages sur les différents channels websockets
    """
    @database_sync_to_async
    def create_message(self, contenu: str, id_conversation: int, id_utilisateur: int) -> Message:
        """
        Créer un message en asynchrone dans la base de données
        """
        return Message.objects.create(contenu=contenu, conversation_id=id_conversation, utilisateur_id=id_utilisateur)

    async def connect(self):
        """
        Etablie une connexion avec le websocket
        """
        self.id_conversation = self.scope['url_route']['kwargs']['id_conversation']
        self.conversation_group_name = 'chat_%s' % self.id_conversation
        print('Connect to groupName : ', self.id_conversation)
        await self.channel_layer.group_add(
            self.id_conversation,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, code: str):
        """Est appelé lorsque la connexion avec le websocket est fermé

        Args:
            code (str): Code de déconnexion
        """
        await self.channel_layer.group_discard(
            self.id_conversation,
            self.channel_name
        )

    async def receive(self, text_data: object):
        """Est appelé lorsqu'on reçoit un message d'un client connecté au websocket

        Args:
            text_data (object): Données reçu du client du websocket
        """
        print('Receive Message : ', text_data)
        message_json: dict = json.loads(text_data)
        contenu = message_json['contenu']
        id_conversation = message_json['id_conversation']
        id_utilisateur = message_json['utilisateur']['id']
        nom_utilisateur = message_json['utilisateur']['nom']
        date_heure = message_json['date_heure']

         # Envoie le message dans la conversation
        await self.channel_layer.group_send(
            self.id_conversation, {
                'type': 'send_message',
                'contenu': contenu,
                'id_conversation': id_conversation,
                'utilisateur': {
                    'id': id_utilisateur,
                    'nom': nom_utilisateur,
                },
                'date_heure': date_heure
        })

    async def send_message(self, event: dict):
        """Est appelé lorsqu'on reçoit un message du groupe du channel @see receive

        Args:
            event (dict): Evènement/Message réçu d'un des client websocket du groupe
        """
        print('Send Message : ', event)
        contenu = event['contenu']
        id_conversation = event['id_conversation']
        id_utilisateur = event['utilisateur']['id']
        nom_utilisateur = event['utilisateur']['nom']

        message: Message = await self.create_message(contenu, id_conversation, id_utilisateur)
        print('Message in database : ', message)

        # Envoie le message au websocket
        await self.send(text_data=json.dumps({
                'contenu': contenu,
                'id_conversation': id_conversation,
                'utilisateur': {
                    'id': id_utilisateur,
                    'nom': nom_utilisateur,
                },
                'date_heure': dateformat.format(message.date_heure, 'd F Y H:i')
        }))
