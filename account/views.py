from django.shortcuts import render
from django.views.generic import CreateView, UpdateView
from account.forms import SignUpForm, UpdateForm
from django.urls import reverse_lazy
from django.conf import settings
from django.contrib.auth import get_user_model
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

def accountView(request):
    user = request.user

    context = {'user': user}
    return render(request, 'registration/account.html', context)

class UserUpdate(UpdateView):
    model = get_user_model()
    form_class = UpdateForm
    pk_url_kwarg = 'id'
    template_name = 'registration/update.html'
    success_url = reverse_lazy('profile')