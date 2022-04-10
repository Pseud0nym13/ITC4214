from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from .models import Games, User
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models import Q


def profile(request):
    return
class Profile(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = User
    fields = ['first_name','last_name', 'email']
    template_name= 'profile.html'

class GameCreateView(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Games
    fields = ['name','genre','description','release_date']
    template_name = 'addgame.html'
    success_url = 'games'
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
    
class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'register.html'
    success_url = '/'
    
class LogoutInterfaceView(LoginRequiredMixin, LogoutView):
    login_url = '/login/'
    template_name ='logout.html'

class LoginInterfaceView(LoginView):
    template_name ='login.html'

def home(request):
    return render(request, 'home.html')
class GameList(ListView):
    model = Games
    template_name = 'games.html'
    context_object_name = 'games'
    def get_queryset(self):
        search = self.request.GET.get('search')
        if search: 
            return Games.objects.filter(Q(name__icontains= search) | Q(genre__name__icontains= search) ) 
        return Games.objects.all()

# Create your views here.
