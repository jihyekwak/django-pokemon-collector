from django.contrib import admin
from .models import Pokemon, PokemonMove, League

# Register your models here.

admin.site.register(Pokemon)
admin.site.register(PokemonMove)
admin.site.register(League)