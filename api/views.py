from django.shortcuts import render
from esieechat.models import Conversation, Message
from .serializers import MessagesSerializer
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here
# class MessageListView(viewsets.ModelViewSet):
#     queryset = Message.objects.all()
#     serializer_class = MessagesSerializer
#     filterset_fields = ["conversation_id"]
class MessageList(APIView):
    def get(self, request, conversation_id):
        messages = Message.objects.filter(conversation_id=conversation_id)
        serializer = MessagesSerializer(messages, many=True)
        return Response(serializer.data)