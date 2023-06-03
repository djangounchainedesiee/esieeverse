from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views
from .views import CustomLoginView

app_name = 'auth'

urlpatterns =[	
  #path('accounts/', include('django.contrib.auth.urls')),
  #path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),	
  #path('logout/', views.logout_view, name='logout'),
  path('signup/', views.signup, name='signup'),
  path('login/', CustomLoginView.as_view(), name='login'),
  path('logout/', LogoutView.as_view(), name='logout')
]