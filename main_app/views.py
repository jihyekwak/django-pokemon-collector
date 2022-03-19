from django.shortcuts import render
from django.views.generic.base import TemplateView
# from django.views import View
# from django.http import HttpResponse

# class Home(View):
#     def get(self, request):
#         return HttpResponse("Pokemon Collector")

class Home(TemplateView):
    template_name='home.html'

class Pokemon:
    def __init__(self, name, type):
        self.name = name
        self.type = type

pokemons = [
    Pokemon("Pikachu", "Electric")
]

class Index(TemplateView):
    template_name='index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pokemons']= pokemons
        return context