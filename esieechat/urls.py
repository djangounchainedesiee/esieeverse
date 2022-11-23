from django.urls import path
from . import views


app_name = 'esieechat'

urlpatterns = [
    path('create', views.create_conversation),
]

# path('conversation/<int:id>/', views.conversation, name='conversation')
# path('message/<int:id>/', views.message, name='message')