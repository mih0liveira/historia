from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from app.views import *
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
     path('cidade/', CidadesView.as_view(), name='cidades'),
    path('personagem/', PersonagensHistoricosView.as_view(), name='personagens'),
    path('documento/', DocumentosHistoricosView.as_view(), name='documentos'),
    path('evento/', EventosHistoricosView.as_view(), name='eventos'),
    path('tipo/', TiposDocumentosView.as_view(), name='tipos_documentos'),
    path('area/', AreasSaberView.as_view(), name='areas_saber'),
    path('usuario/', UsuariosView.as_view(), name='usuarios'),
    path('linha/', LinhasDoTempoView.as_view(), name='linhas_tempo'),
    path('ocupacao/', OcupacoesView.as_view(), name='ocupacoes'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)