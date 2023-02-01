from django.urls import path
from . import views

app_name = 'publication'

urlpatterns = [
    path('', views.display, name='root'),
    path('like/', views.display, name='like'),
    path('disklike/', views.display, name='dislike'),
]
