from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from .models import Game
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
games = [
    {
    'developer':'Maple Sapling',
    'name' : 'Bio',
    'genre': 'JRPG',
    'Description': 'blabla',
    'date_posted': 'August 27, 2022',
    'release_date': 'August 27, 2022',
    }
        ]
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

def games(request):
    context = {
        'games': Game.objects.all()
    }
    return render (request, 'games.html', context)

# Create your views here.
