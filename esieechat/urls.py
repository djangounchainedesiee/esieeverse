from django.urls import path, include
from . import views

app_name = 'esieechat'

urlpatterns = [
    path('create/', views.create_conversation, name="create"),
    path('select/', views.select_conversation, name="select"),
    path('view/<str:id_conversation>/', views.view_conversation, name="view"),
    path('<str:id_conversation>/people/add/', views.add_people_in_conversation, name="add_people"),
    path('<str:id_conversation>/people/delete/<str:id_utilisateur>/', views.delete_people_in_conversation, name="delete_people"),
]