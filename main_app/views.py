from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from sre_constants import SUCCESS
from .models import Pokemon, Move, League
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# from django.views import View
# from django.http import HttpResponse

# class Home(View):
#     def get(self, request):
#         return HttpResponse("Pokemon Collector")

class Home(TemplateView):
    template_name='home.html'

class About(TemplateView):
    template_name='about.html'

# class Pokemon:
#     def __init__(self, name, type, description, abilities=[],is_collected = False ):
#         self.name = name
#         self.type = type
#         self.description = description
#         self.abilities = abilities
#         self.is_collected = is_collected

# pokemons = [
#     Pokemon("Pikachu", "Electric", 'Pikachu that can generate powerful electricity have cheek sacs that are extra soft and super stretchy.', ['Static'], True ),
#     Pokemon("Eevee", "Normal", 'Eight different Pokemon evolve from the amazingly adaptive Eevee, accrogind to current stuies. It has the ability to alter the composition of its body to suit its surrounding environment.', ['Run Away', 'Adaptability'], False ),
#     Pokemon("Togepi", "Normal", 'The shell seems to be filled with joy. It is said that it will share good luck when treated kindly.', ['Serene Grace', 'Hustle'], True ),
#     Pokemon("Clefairy", "Fairy", 'It is said that happiness will come to those who see a gathering of Clefairy dancing under a full moon.', ['Cute Charm', 'Nagic Guard'], True),
#     Pokemon("Snorlax", "Normal", 'It is not satisfied unless it eats over 880 pounds of food every day. When it is done eating, it goes promptly to sleep.', ['Thick Fat', 'Immunity'], True),
#     Pokemon("Charizard", "Fire", 'It spits fire that is hot enough to melt boulders. It may cause forest fires by blowing flames.', ['Blaze'], True),
#     Pokemon("Piplup", "Water", 'It doesn’t like to be taken care of. It’s difficult to bond with since it won’t listen to its Trainer.', ['Torrent'], True)
# ]

# collected_pokemons = [pokemon for pokemon in pokemons if pokemon.is_collected]


# Pokemon

class Index(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        name = self.request.GET.get("name")
        if name != None:
            context['pokemons'] = Pokemon.objects.filter(name__icontains=name)
            context['header'] = f"Searching for {name}"
        else:
            context['pokemons']= Pokemon.objects.all()
            context['header']= "Index of Pokemon"
        return context

class Detail(DetailView, DeleteView):
    model = Pokemon
    fields = ['name', 'img', 'type', 'description', 'abilities', 'moves', 'gender', 'evolved', 'user', 'leagues']
    template_name = "detail.html"
    success_url = "/index/"

class Create(CreateView):
    model = Pokemon
    fields = ['name', 'img', 'type', 'description','gender', 'evolved', 'user']
    template_name= "create.html"
    success_url ="/index/"

    def from_valid(self, form):
        self.object = form.save(commit = False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect('/index/')

class Update(UpdateView):
    model = Pokemon
    fields = ['name', 'img', 'type', 'description', 'abilities',  'moves', 'gender', 'evolved', 'user', 'leagues']
    template_name = "update.html"
    def get_success_url(self):
        return reverse('detail', kwargs = {'pk': self.object.pk})


# User

def profile(request, username):
    user = User.objects.get(username = username)
    pokemons = Pokemon.objects.filter(user = user)
    return render(request, 'profile.html', {'username': username.capitalize(), 'pokemons': pokemons})

def users(request):
    users = User.objects.all()
    return render(request, 'users.html', {'users':users})


# PokemonMove

def moves_index(request):
    moves = Move.objects.all()
    return render(request, 'moves_index.html', {'moves': moves})

def move_show(request, move_id):
    move = Move.objects.get(id = move_id)
    return render(request, 'move_show.html', {'move': move})

class Move_Create(CreateView):
    model = Move
    fields = '__all__'
    template_name = 'move_create.html'
    success_url = "/moves/"

class Move_Update(UpdateView):
    models = Move
    fields = ['name', 'type']
    template_name = 'move_update.html'
    success_url = "/moves/"

    def get_queryset(self):
        return Move.objects.all()

class Move_Delete(DeleteView):
    models = Move
    template_name = 'move_delete_confirmation.html'
    success_url = "/moves/"

    def get_queryset(self):
        return Move.objects.all()

# League

def leagues_index(request):
    leagues = League.objects.all()
    return render(request, 'leagues_index.html', {'leagues': leagues})

# def league_show(request, league_id):
#     league = League.objects.get(id=league_id)
#     return render(request, 'league_show.html', {'league': league})

class League_Create(CreateView):
    model = League
    fields = '__all__'
    template_name = 'league_create.html'
    success_url = "/leagues/"

class League_Update(UpdateView):
    model = League
    fields = ['name']
    template_name = 'league_update.html'
    success_url = "/leagues/"

class League_Delete(DeleteView):
    model = League
    template_name = 'league_delete_confirmation.html'
    success_url = "/leagues/"