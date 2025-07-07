
from django.views import View
from django.contrib import messages
from django.shortcuts import render
from .models import (
    Cidade, PersonagemHistorico, DocumentoHistorico, EventoHistorico,
    TipoDocumento, AreaSaber, Usuario, LinhaDoTempo, Ocupacao
)
class IndexView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
    def post(self, request):
        pass
class CidadesView(View):
    def get(self, request, *args, **kwargs):
        cidades = Cidade.objects.all()
        return render(request, 'cidade.html', {'cidades': cidades})

class PersonagensHistoricosView(View):
    def get(self, request, *args, **kwargs):
        personagens = PersonagemHistorico.objects.all()
        return render(request, 'personagem.html', {'personagens': personagens})

class DocumentosHistoricosView(View):
    def get(self, request, *args, **kwargs):
        documentos = DocumentoHistorico.objects.all()
        return render(request, 'documento.html', {'documentos': documentos})

class EventosHistoricosView(View):
    def get(self, request, *args, **kwargs):
        eventos = EventoHistorico.objects.all()
        return render(request, 'evento.html', {'eventos': eventos})

class TiposDocumentosView(View):
    def get(self, request, *args, **kwargs):
        tipos_documentos = TipoDocumento.objects.all()
        return render(request, 'tipo.html', {'tipos_documentos': tipos_documentos})

class AreasSaberView(View):
    def get(self, request, *args, **kwargs):
        areas = AreaSaber.objects.all()
        return render(request, 'area.html', {'areas': areas})

class UsuariosView(View):
    def get(self, request, *args, **kwargs):
        usuarios = Usuario.objects.all()
        return render(request, 'usuario.html', {'usuarios': usuarios})

class LinhasDoTempoView(View):
    def get(self, request, *args, **kwargs):
        linhas = LinhaDoTempo.objects.all()
        return render(request, 'linha.html', {'linhas': linhas})

class OcupacoesView(View):
    def get(self, request, *args, **kwargs):
        ocupacoes = Ocupacao.objects.all()
        return render(request, 'ocupacao.html', {'ocupacoes': ocupacoes})

