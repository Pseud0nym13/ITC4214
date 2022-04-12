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
from django.contrib.auth.decorators import login_required
@login_required(login_url='login')
def update(request, sys_gen_user):

    # here I am getting the user name of current logged in user.
    if request.user.is_authenticated:
        username = request.user.username

    if username == sys_gen_user:
        user_id = User.objects.get(sys_gen_user=sys_gen_user)
        if request.method == 'GET':
            form = CustomUserCreationForm(instance=user_id)
            return render(request, 'update.html', {'form': form})
        else:
            form = CustomUserCreationForm(request.POST, instance=user_id)
            if form.is_valid():
                form.save()
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
    fields = ['name','genre','description','release_date', 'image']
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
