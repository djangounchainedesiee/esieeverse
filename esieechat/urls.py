from django.urls import path, include
from . import views

app_name = 'esieechat'

urlpatterns = [
    path('create/', views.create_conversation, name="create"),
    path('create/<int:id_utilisateur>/', views.create_or_join_conversation_with_user, name="create_join_conv_user"),
    path('edit/<int:id_conversation>/', views.edit_conversation, name="edit"),
    path('select/', views.select_conversation, name="select"),
    path('view/<int:id_conversation>/', views.view_conversation, name="view"),
    path('<int:id_conversation>/people/add/', views.add_people_in_conversation, name="add_people"),
    path('<int:id_conversation>/people/delete/<int:id_utilisateur>/', views.delete_people_in_conversation, name="delete_people"),
]