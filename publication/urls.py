from django.urls import path
from . import views

app_name = 'publication'

urlpatterns = [
    path('like/<int:id_publication>/', views.like, name='like'),
    path('dislike/<int:id_publication>/', views.dislike, name='dislike'),
    path('inscrire/<int:id_evenement>/', views.inscrire_evenement, name='inscrire_evenement'),
    path('desinscrire/<int:id_evenement>/', views.desinscrire_evenement, name='desinscrire_evenement'),
]
