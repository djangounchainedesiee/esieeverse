from django.urls import path
from . import consumers

"""
Route des urls vers les channels websoclets
"""

websocket_urlpatterns = [
    path('ws/chat/<str:conversation_id>/', consumers.ChatConsumer.as_asgi())
]