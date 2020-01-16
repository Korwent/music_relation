from django.shortcuts import render
from django.http import HttpResponse
from .models import Personne, Groupe, SensInstrument, Instrument, ModeleInstrument, ExemplaireInstrument, TypeSortie, EtapeSortie, CycleSortie, Sortie, ReseauxSociauxPersonne, ReseauxSociauxGroupe

def index(request):
    return HttpResponse("Hello, world. You're at the possibility_test index.")
