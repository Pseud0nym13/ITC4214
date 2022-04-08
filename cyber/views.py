from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
def logout(request):
    auth.logout(request)
    return redirect('/')

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = 'home.html'
    
class LogoutInterfaceView(LogoutView):
    template_name ='logout.html'

class LoginInterfaceView(LoginView):
    template_name ='login.html'

def home(request):
    return render(request, 'home.html')

# Create your views here.
