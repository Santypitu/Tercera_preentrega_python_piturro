from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=100)
    numero_pokedex = models.PositiveIntegerField()

class Tipo(models.Model):
    nombre = models.CharField(max_length=50)
    pokemon = models.ManyToManyField(Pokemon)

class Habilidad(models.Model):
    nombre = models.CharField(max_length=100)
    pokemon = models.ManyToManyField(Pokemon)