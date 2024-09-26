from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PokemonForm, TipoForm, HabilidadForm
from .models import Pokemon, Tipo, Habilidad

from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PokemonForm, TipoForm, HabilidadForm
from .models import Pokemon, Tipo, Habilidad

def index(request):
    if request.method == 'POST':
        pokemon_form = PokemonForm(request.POST)
        tipo_form = TipoForm(request.POST)
        habilidad_form = HabilidadForm(request.POST)

        if pokemon_form.is_valid() and tipo_form.is_valid() and habilidad_form.is_valid():
            nuevo_pokemon = pokemon_form.save()
            nuevo_tipo = tipo_form.save()
            nuevo_habilidad = habilidad_form.save()

            # Asociar el tipo y la habilidad al Pokémon
            nuevo_pokemon.tipo = nuevo_tipo
            nuevo_pokemon.habilidad = nuevo_habilidad
            nuevo_pokemon.save()  # Guardar los cambios

            return HttpResponseRedirect('/')  # Redirigir a la página principal

    else:
        pokemon_form = PokemonForm()
        tipo_form = TipoForm()
        habilidad_form = HabilidadForm()

    return render(request, 'pokedex/index.html', {
        'pokemon_form': pokemon_form,
        'tipo_form': tipo_form,
        'habilidad_form': habilidad_form,
    })

def pokedex_pag(request):
    resultados = []
    if 'query' in request.GET:
        query = request.GET['query']
        resultados = Pokemon.objects.filter(nombre__icontains=query)
    else:
        resultados = Pokemon.objects.all()
    return render(request, 'pokedex/pokedex_pag.html', {'resultados': resultados, 'query': query})