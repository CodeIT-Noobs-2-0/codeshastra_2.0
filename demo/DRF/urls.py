from django.urls import path, include
from knox import views as knox_views
from .api import *
from rest_framework import routers
from rest_framework.authtoken import views as authtoken_views

urlpatterns = [
    path('users-display/', UserDisplayView.as_view(), name='user-display-all'),
    path('users-display/<int:pk>/', UserDisplayView.as_view(), name='user-display-single'),
    path('user-register/', RegisterUser.as_view(), name='user-register'),
    path('', include('rest_framework.urls')),
    path('login/', LoginView.as_view(), name='knox_login'),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall'),
    path('api-token-auth/', authtoken_views.obtain_auth_token, name='api-tokn-auth'), 
]