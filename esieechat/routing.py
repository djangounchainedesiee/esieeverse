from django.urls import path
from . import consumers

"""
Route des urls vers les channels websoclets
"""

websocket_urlpatterns = [
    path('ws/chat/<str:id_conversation>/', consumers.ChatConsumer.as_asgi())
]