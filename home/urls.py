from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path('', views.home_view, name='home_view'),
    path('add_friend/<int:id_utilisateur>/', views.add_friend, name='add_friend'),
]