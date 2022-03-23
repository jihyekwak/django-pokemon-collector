# Generated by Django 4.0.3 on 2022-03-23 06:04

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('img', models.CharField(max_length=250)),
                ('type', models.CharField(choices=[('ice', 'Ice'), ('ground', 'Ground'), ('fighting', 'Fighting'), ('dark', 'Dark'), ('fairy', 'Fairy'), ('steel', 'Steel'), ('psychic', 'Psychic'), ('water', 'Water'), ('rock', 'Rock'), ('electric', 'Electric'), ('dragon', 'Dragon'), ('bug', 'Bug'), ('fire', 'Fire'), ('normal', 'Normal'), ('flying', 'Flying'), ('grass', 'Grass'), ('posion', 'Poison')], max_length=10)),
                ('description', models.TextField(blank=True)),
                ('abilities', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=20), blank=True, size=None)),
                ('collected', models.BooleanField(default=False)),
                ('evolved', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]