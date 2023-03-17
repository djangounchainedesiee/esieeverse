from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = [
    path('abonnements/', views.Abonnements.as_view(), name="abonnements"),
    path('choixs/', views.Choixs.as_view(), name="choix"),
    path('evenements/<int:id_evenement>/choixs/', views.getAllChoixsWithTotalVotesByEvenement, name="choixs_by_evenement"),
]

urlpatterns = format_suffix_patterns(urlpatterns)