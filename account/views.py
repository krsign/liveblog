from django.shortcuts import render
from django.views.generic import CreateView
from account.forms import SignUpForm
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth import authenticate, login
class SignUpView(CreateView):
    model = settings.AUTH_USER_MODEL
    form_class = SignUpForm  
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('home')
    
    
    # for automatic login after signup
    def form_valid(self, form):
        result = super().form_valid(form)
        cd = form.cleaned_data
        user = authenticate(username=cd['username'], password=cd['password1'])
        login(self.request, user)
        return result