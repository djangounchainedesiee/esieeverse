from django.urls import path
from . import views

app_name = 'publication'

urlpatterns = [
    path('like/<int:id_publication>/', views.like, name='like'),
    path('dislike/<int:id_publication>/', views.dislike, name='dislike'),
]
