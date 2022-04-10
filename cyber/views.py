from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from .models import Games
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
def logout(request):
    AuthenticationError.logout(request)
    return redirect('/')

def profile(request):
    return

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

def display_games(request):
    all_games = Games.objects.all()
    return render(request,'games.html', {'games' : all_games})

    

# Create your views here.
