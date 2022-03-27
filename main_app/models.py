from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

# Create your models here.

class League(models.Model):

    name = models.CharField(max_length = 20, blank = True)

    def __str__(self):
        return self.name

MOVETYPE_CHOICES = {
    ('Physical', 'Physical'),
    ('Special', 'Special'),
    ('Status', 'Status')
}

class Move(models.Model):

    name = models.CharField(max_length=10)
    type = models.CharField(max_length = 10, choices = MOVETYPE_CHOICES)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['type']

TYPE_CHOICES = {
    ("Bug", "Bug"),
    ("Dark", "Dark"),
    ("Dragon", "Dragon"),
    ("Electric", "Electric"),
    ("Fairy", "Fairy"),
    ("Fighting", "Fighting"),
    ("Fire", "Fire"),
    ("Flying", "Flying"),
    ("Grass", "Grass"),
    ("Ground", "Ground"),
    ("Ice", "Ice"),
    ("Normal", "Normal"),
    ("Posion", "Poison"),
    ("Psychic", "Psychic"),
    ("Rock", "Rock"),
    ("Steel", "Steel"),
    ("Water", "Water"),
}

GENDER_CHOICES = {
    ("Male", "Male"),
    ("Female", "Female")
}

class Pokemon(models.Model):

    name = models.CharField(max_length = 20)
    img = models.CharField(max_length = 250)
    type = models.CharField(max_length = 10, choices = TYPE_CHOICES)
    description = models.TextField(blank = True)
    abilities = ArrayField(models.CharField(max_length = 20), blank = True)
    moves = models.ManyToManyField(Move, blank = True)
    gender = models.CharField(max_length = 10, choices = GENDER_CHOICES)
    evolved = models.BooleanField(default = False)
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    leagues = models.ManyToManyField(League, blank = True)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']