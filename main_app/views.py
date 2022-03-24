from django.shortcuts import render
from django.urls import reverse
from sre_constants import SUCCESS
from .models import Pokemon
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

class Index(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemons']= Pokemon.objects.all()
        return context

class Collection(TemplateView):
    template_name = 'collection.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemons']= Pokemon.objects.filter(collected = True)
        return context

class Create(CreateView):
    model = Pokemon
    fields = ['name', 'img', 'type', 'description', 'abilities', 'evolved', 'collected']
    template_name= "create.html"
    success_url ="/index/"

class Detail(DetailView, DeleteView):
    model = Pokemon
    fields = ['name', 'img', 'type', 'description', 'abilities', 'evolved', 'collected']
    template_name = "detail.html"
    success_url = "/index/"

class Update(UpdateView):
    model = Pokemon
    fields = ['name', 'img', 'type', 'description', 'abilities', 'evolved', 'collected']
    template_name = "update.html"
    def get_success_url(self):
        return reverse('detail', kwargs = {'pk': self.object.pk})
