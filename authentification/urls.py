from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'auth'

urlpatterns =[
	
	path('accounts/', include('django.contrib.auth.urls')),
	path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),	
	path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name = 'logout'),
    path('register/', views.register, name='register'),
]