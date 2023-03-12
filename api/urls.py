from django.urls import include, path
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

app_name = 'api'

urlpatterns = [
    path('abonnements/', views.Abonnements.as_view(), name="abonnements"),
]

urlpatterns = format_suffix_patterns(urlpatterns)