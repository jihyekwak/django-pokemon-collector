from django.contrib import admin
from .models import Pokemon, Move, League

# Register your models here.

admin.site.register(Pokemon)
admin.site.register(Move)
admin.site.register(League)