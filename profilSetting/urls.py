from django.urls import path, include
from . import views

app_name = 'profilSetting'

urlpatterns = [
    path('', views.profil_setting, name="profil_setting"),
    
    
]