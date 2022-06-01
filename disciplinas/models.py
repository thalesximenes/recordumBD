from django.db import models
from usuarios.models import Usuario
from datetime import datetime

class Disciplinas(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    thumb = models.ImageField(upload_to = "thumb_Disciplinas")

    def __str__(self) -> str:
        return self.nome

class Aulas(models.Model):
    nome = models.CharField(max_length = 100)
    descricao = models.TextField()
    aula = models.FileField(upload_to = "aulas", blank=True)
    disciplina = models.ForeignKey(Disciplinas, on_delete = models.DO_NOTHING)

    def __str__(self) -> str:
        return self.nome

class MapasMentai(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete = models.DO_NOTHING)
    mapa = models.ImageField(upload_to = "mapa_Usuario")
    data = models.DateTimeField(default = datetime.now)
    aula = models.ForeignKey(Aulas, on_delete = models.DO_NOTHING)
    
    def __str__(self) -> str:
        return self.usuario.nome