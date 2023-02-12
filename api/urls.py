from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

#router = routers.DefaultRouter()
# router.register(r'messageList', views.MessageList.get)
# path('', include(router.urls))

urlpatterns = [
    #path('', include(router.urls)),
    path('messageList/<int:conversation_id>', views.MessageList.as_view(), name="api_conversation_list"),
]

urlpatterns = format_suffix_patterns(urlpatterns)