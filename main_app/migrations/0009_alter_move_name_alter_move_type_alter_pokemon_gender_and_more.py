# Generated by Django 4.0.3 on 2022-03-31 21:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0008_rename_pokemon_move_move_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='move',
            name='name',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='move',
            name='type',
            field=models.CharField(choices=[('Status', 'Status'), ('Physical', 'Physical'), ('Special', 'Special')], max_length=20),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=10),
        ),
        migrations.AlterField(
            model_name='pokemon',
            name='type',
            field=models.CharField(choices=[('Steel', 'Steel'), ('Ice', 'Ice'), ('Flying', 'Flying'), ('Water', 'Water'), ('Dark', 'Dark'), ('Ground', 'Ground'), ('Rock', 'Rock'), ('Normal', 'Normal'), ('Fire', 'Fire'), ('Bug', 'Bug'), ('Fighting', 'Fighting'), ('Posion', 'Poison'), ('Dragon', 'Dragon'), ('Electric', 'Electric'), ('Psychic', 'Psychic'), ('Fairy', 'Fairy'), ('Grass', 'Grass')], max_length=20),
        ),
    ]
