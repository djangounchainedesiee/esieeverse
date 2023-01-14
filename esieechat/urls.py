from django.urls import path
from . import views


app_name = 'esieechat'

urlpatterns = [
    path('create/', views.create_conversation, name="create"),
    path('select/', views.select_conversation, name="select"),
    path('view/<str:id>/', views.view_conversation, name="view"),
    path('<str:id>/people/add/', views.add_people_in_conversation, name="add_people")
]

# path('conversation/<int:id>/', views.conversation, name='conversation')
# path('message/<int:id>/', views.message, name='message')