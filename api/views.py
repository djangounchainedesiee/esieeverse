from django.shortcuts import render
from esieechat.models import Conversation, Message
from .serializers import MessagesSerializer
from rest_framework import viewsets

# Create your views here
class MessageListView(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessagesSerializer
    filterset_fields = ["conversation_id"]