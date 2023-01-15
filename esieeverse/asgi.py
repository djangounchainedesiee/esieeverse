from django.core.asgi import get_asgi_application
from channels.auth import AuthMiddlewareStack
from channels.routing import ProtocolTypeRouter, URLRouter
from esieechat.routing import websocket_urlpatterns
import os

# application = ProtocolTypeRouter({
#     'http': get_asgi_application(),
#     'websocket': URLRouter(
#         urlpatterns
#     )
# })

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'esieeverse.settings')

application = ProtocolTypeRouter( 
    {
        "http": get_asgi_application(),
        "websocket": AuthMiddlewareStack(
            URLRouter(
               websocket_urlpatterns
            )
        ),
    }
)