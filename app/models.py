from django.db import models

class Cidade(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome da cidade")
    uf = models.CharField(max_length=2, verbose_name="UF")

    def __str__(self):
        return f"{self.nome}, {self.uf}"

    class Meta:
        verbose_name = "Cidade"
        verbose_name_plural = "Cidades"


class TipoDocumento(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Tipo de Documento")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Tipo de Documento"
        verbose_name_plural = "Tipos de Documento"


class AreaSaber(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Área do Saber")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Área do Saber"
        verbose_name_plural = "Áreas do Saber"



class EventoHistorico(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Evento")
    descricao = models.TextField(verbose_name="Descrição")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_fim = models.DateField(verbose_name="Data de Fim")
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, verbose_name="Cidade")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Evento Histórico"
        verbose_name_plural = "Eventos Históricos"


class PersonagemHistorico(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome do Personagem")
    biografia = models.TextField(verbose_name="Biografia")
    data_nasc = models.DateField(verbose_name="Data de Nascimento")
    data_falecimento = models.DateField(null=True, blank=True, verbose_name="Data de Falecimento")
    cidade = models.ForeignKey(Cidade, on_delete=models.SET_NULL, null=True, verbose_name="Cidade Natal")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Personagem Histórico"
        verbose_name_plural = "Personagens Históricos"


class DocumentoHistorico(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Título")
    descricao = models.TextField(verbose_name="Descrição")
    data_documento = models.DateField(verbose_name="Data do Documento")
    imagem = models.ImageField(upload_to='documentos/', null=True, blank=True, verbose_name="Imagem")
    tipo_documento = models.ForeignKey(TipoDocumento, on_delete=models.SET_NULL, null=True, verbose_name="Tipo de Documento")
    evento = models.ForeignKey(EventoHistorico, on_delete=models.SET_NULL, null=True, verbose_name="Evento Histórico")
    personagem = models.ForeignKey(PersonagemHistorico, on_delete=models.SET_NULL, null=True, verbose_name="Personagem Histórico")

    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name = "Documento Histórico"
        verbose_name_plural = "Documentos Históricos"


class LinhaDoTempo(models.Model):
    nome = models.CharField(max_length=200, verbose_name="Nome da Linha do Tempo")
    data_inicio = models.DateField(verbose_name="Data de Início")
    data_final = models.DateField(verbose_name="Data Final")
    eventos = models.ManyToManyField(EventoHistorico, verbose_name="Eventos Históricos")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Linha do Tempo"
        verbose_name_plural = "Linhas do Tempo"

class Ocupacao(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Ocupação"
        verbose_name_plural = "Ocupações"

class Usuario(models.Model):
    nome = models.CharField(max_length=100, verbose_name="Nome")
    email = models.EmailField(verbose_name="Email")
    senha = models.CharField(max_length=128, verbose_name="Senha")
    ocupacao = models.ForeignKey(Ocupacao, on_delete=models.SET_NULL, null=True, blank=True, verbose_name="Ocupação")

    def __str__(self):
        return self.nome

    class Meta:
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"



