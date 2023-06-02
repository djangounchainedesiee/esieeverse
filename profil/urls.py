from django.urls import path
from . import views

app_name = 'profil'

urlpatterns = [
    path('<int:id_utilisateur>/', views.view_profil, name='view_profil'),
    path('<int:id_utilisateur>/add_friend/', views.add_friend, name='add_friend'),
    path('<int:id_utilisateur>/voter/<int:id_choix>/', views.voter, name='voter'),
]