from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from .models import Games, User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView

def logout(request):
    AuthenticationError.logout(request)
    return redirect('/')
def profile(request):
    return
class Profile(UpdateView):
    model = User
    fields = ['first_name','last_name', 'email']
    template_name= 'profile.html'

class GameCreateView(CreateView):
    model = Games
    fields = ['name','genre','description','release_date']
    template_name = 'addgame.html'
    success_url = 'games'

class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = 'home'
    
class LogoutInterfaceView(LogoutView):
    template_name ='logout.html'

class LoginInterfaceView(LoginView):
    template_name ='login.html'

def home(request):
    return render(request, 'home.html')
def games(request):
    context = {
        'games': Games.objects.all()
    }
    return render (request, 'games.html', context)

# Create your views here.
