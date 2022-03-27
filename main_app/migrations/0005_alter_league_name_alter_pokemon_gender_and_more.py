# Generated by Django 4.0.3 on 2022-03-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_league_pokemonmove_remove_pokemon_battle_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='league',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='leagues',
            field=models.ManyToManyField(blank=True, to='main_app.league'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='moves',
            field=models.ManyToManyField(blank=True, to='main_app.pokemonmove'),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('Fire', 'Fire'), ('Bug', 'Bug'), ('Ground', 'Ground'), ('Grass', 'Grass'), ('Fairy', 'Fairy'), ('Posion', 'Poison'), ('Dark', 'Dark'), ('Psychic', 'Psychic'), ('Electric', 'Electric'), ('Dragon', 'Dragon'), ('Flying', 'Flying'), ('Normal', 'Normal'), ('Ice', 'Ice'), ('Fighting', 'Fighting'), ('Steel', 'Steel'), ('Rock', 'Rock'), ('Water', 'Water')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pokemonmove',
            name='type',
            field=models.CharField(choices=[('Special', 'Special'), ('Status', 'Status'), ('Physical', 'Physical')], max_length=10),
        ),
    ]
