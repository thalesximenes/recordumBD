from django.db import models
from django.contrib.auth.models import User
from rest_framework import serializers

class Informacoe(models.Model):
    usuario = models.ForeignKey(User, on_delete = models.DO_NOTHING, primary_key=True)
    escolaridade = models.CharField(max_length=100)
    vestibulares = models.CharField(max_length=100)
    curso = models.CharField(max_length=100)
    universidade = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.nome

class InformacoesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Informacoe
        fields = "__all__"
