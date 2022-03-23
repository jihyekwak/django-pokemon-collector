from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.

TYPE_CHOICES = {
    ("bug", "Bug"),
    ("dark", "Dark"),
    ("dragon", "Dragon"),
    ("electric", "Electric"),
    ("fairy", "Fairy"),
    ("fighting", "Fighting"),
    ("fire", "Fire"),
    ("flying", "Flying"),
    ("grass", "Grass"),
    ("ground", "Ground"),
    ("ice", "Ice"),
    ("normal", "Normal"),
    ("posion", "Poison"),
    ("psychic", "Psychic"),
    ("rock", "Rock"),
    ("steel", "Steel"),
    ("water", "Water"),
}

class Pokemon(models.Model):

    name = models.CharField(max_length = 20)
    img = models.CharField(max_length = 250)
    type = models.CharField(max_length = 10, choices = TYPE_CHOICES)
    description = models.TextField(blank = True)
    abilities = ArrayField(models.CharField(max_length = 20), blank = True)
    collected = models.BooleanField(default = False)
    evolved = models.BooleanField(default = False)
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['name']