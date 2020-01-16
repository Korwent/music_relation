from django.contrib import admin

from .models import Personne, Groupe, SensInstrument, Instrument, ModeleInstrument, ExemplaireInstrument, TypeSortie, EtapeSortie, CycleSortie, Sortie, ReseauxSociauxPersonne, ReseauxSociauxGroupe

@admin.register(Groupe)
@admin.register(Personne)
@admin.register(Instrument)
@admin.register(SensInstrument)
@admin.register(ModeleInstrument)
@admin.register(ExemplaireInstrument)
@admin.register(ReseauxSociauxPersonne)
@admin.register(ReseauxSociauxGroupe)
@admin.register(TypeSortie)
@admin.register(EtapeSortie)
@admin.register(CycleSortie)
@admin.register(Sortie)



class PersonneAdmin(admin.ModelAdmin):
    pass
