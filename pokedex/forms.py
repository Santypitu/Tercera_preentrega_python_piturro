from django import forms
from .models import Pokemon, Tipo, Habilidad

class PokemonForm(forms.ModelForm):
  class Meta:
    model = Pokemon
    fields = ['nombre', 'numero_pokedex'] 

class TipoForm(forms.ModelForm):
  class Meta:
    model = Tipo
    fields = ['nombre'] 

class HabilidadForm(forms.ModelForm):
  class Meta:
    model = Habilidad
    fields = ['nombre']  