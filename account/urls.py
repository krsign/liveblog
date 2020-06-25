from django.contrib import admin
from django.urls import path, include
from account.views import SignUpView
from django.contrib.auth.views import LoginView

urlpatterns = [

    path('register', SignUpView.as_view(), name='signup'),
    path('', include('django.contrib.auth.urls')),
   
]