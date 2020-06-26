from django.contrib import admin
from django.urls import path, include
from account.views import SignUpView
from django.contrib.auth.views import LoginView
from account.views import accountView, UserUpdate

urlpatterns = [
    path('profile', accountView, name='profile'),
    path('register', SignUpView.as_view(), name='signup'),
    path('<int:id>', UserUpdate.as_view(), name='userupdate'),
    path('', include('django.contrib.auth.urls')),
   
]