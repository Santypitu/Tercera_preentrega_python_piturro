from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('pokedex/', views.pokedex_pag, name='pokedex_pag'),  
]