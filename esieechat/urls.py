from django.urls import path
from . import views


app_name = 'esieechat'

urlpatterns = [
    path('', views.index),
]

# path('conversation/<int:id>/', views.conversation, name='conversation')
# path('message/<int:id>/', views.message, name='message')