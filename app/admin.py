from django.contrib import admin
from .models import *
from django.contrib import admin
from django.contrib import admin
from .models import LinhaDoTempo

@admin.register(LinhaDoTempo)
class LinhaDoTempoAdmin(admin.ModelAdmin):
    list_display = ("nome", "data_inicio", "data_final")
    filter_horizontal = ("eventos",)
admin.site.register(Cidade)
admin.site.register(TipoDocumento)
admin.site.register(AreaSaber)
admin.site.register(Usuario)
admin.site.register(EventoHistorico)
admin.site.register(PersonagemHistorico)
admin.site.register(DocumentoHistorico)
admin.site.register(Ocupacao)






