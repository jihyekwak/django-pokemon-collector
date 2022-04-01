from types import MethodDescriptorType
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from sre_constants import SUCCESS
from .models import Pokemon, Move, League
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class Home(TemplateView):
    template_name='home.html'

class About(TemplateView):
    template_name='about.html'

class Index(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context['pokemons'] = Pokemon.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name.capitalize()}"
        else:
            context['pokemons']= Pokemon.objects.all()
            context['header']= "Index of Pokemon"
        return context

class Detail(DetailView, DeleteView):
    model = Pokemon
    fields = ['name', 'img', 'type', 'description', 'abilities', 'moves', 'gender', 'evolved', 'user', 'leagues']
    template_name = "detail.html"
    success_url = "/index/"

@method_decorator(login_required, name='dispatch')
class Delete(DeleteView):
    model = Pokemon
    template_name = "delete_confirmation.html"
    success_url = "/index/"

@method_decorator(login_required, name='dispatch')
class Create(CreateView):
    model = Pokemon
    fields = ['name', 'img', 'type', 'description','abilities', 'gender', 'evolved', 'user']
    template_name= "create.html"
    success_url ="/index/"

    def from_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/index/')

@method_decorator(login_required, name='dispatch')
class Update(UpdateView):
    model = Pokemon
    fields = ['name', 'img', 'type', 'description', 'abilities',  'moves', 'gender', 'evolved', 'user', 'leagues']
    template_name = "update.html"
    def get_success_url(self):
        return reverse('detail', kwargs = {'pk': self.object.pk})

# User
@login_required
def profile(request, username):
    user = User.objects.get(username = username)
    pokemons = Pokemon.objects.filter(user = user)
    return render(request, 'profile.html', {'username': username.capitalize(), 'pokemons': pokemons})

@login_required
def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users':users})


# PokemonMove

def moves_index(request):
    moves = Move.objects.all()
    return render(request, 'moves_index.html', {'moves': moves})

# def move_show(request, move_id):
#     move = Move.objects.get(id = move_id)
#     return render(request, 'move_show.html', {'move': move})

@method_decorator(login_required, name='dispatch')
class Move_Create(CreateView):
    model = Move
    fields = '__all__'
    template_name = 'move_create.html'
    success_url = "/moves/"

@method_decorator(login_required, name='dispatch')
class Move_Update(UpdateView):
    model = Move
    fields = ['name', 'type']
    template_name = 'move_update.html'
    success_url = "/moves/"

@method_decorator(login_required, name='dispatch')
class Move_Delete(DeleteView):
    model = Move
    template_name = 'move_delete_confirmation.html'
    success_url = "/moves/"

# League

def leagues_index(request):
    leagues = League.objects.all()
    return render(request, 'leagues_index.html', {'leagues': leagues})

# def league_show(request, league_id):
#     league = League.objects.get(id=league_id)
#     return render(request, 'league_show.html', {'league': league})

@method_decorator(login_required, name='dispatch')
class League_Create(CreateView):
    model = League
    fields = '__all__'
    template_name = 'league_create.html'
    success_url = "/leagues/"

@method_decorator(login_required, name='dispatch')
class League_Update(UpdateView):
    model = League
    fields = ['name']
    template_name = 'league_update.html'
    success_url = "/leagues/"

@method_decorator(login_required, name='dispatch')
class League_Delete(DeleteView):
    model = League
    template_name = 'league_delete_confirmation.html'
    success_url = "/leagues/"

# Login, Logout, Signup
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username = u, password = p)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('/user/' + u)
                else:
                    print('The account has been disabled')
                    return HttpResponseRedirect('/login')
            else:
                print('The username/password is incorrect')
                return HttpResponseRedirect('/login')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/index')
    
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            print('Hello', user.username)
            return HttpResponseRedirect('/user/'+ str(user))
        else:
            HttpResponse('<h1>Try again...</h1>')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})