from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.http import Http404

# Create your views here.

class EixosListView(APIView):
    def get(self, request):
        eixos = EixosTematico.objects.all()
        serializer = EixosSerializer(eixos, many = True)
        return Response(serializer.data)

class DisciplinasListView(APIView):
    def get(self, request):
        disciplinas = Disciplinas.objects.all()
        serializer = DisciplinasSerializer(disciplinas, many = True)
        return Response(serializer.data)

class DisciplinasDetailView(APIView):
    def get_disciplina(self, fk):
        try:
            return Disciplinas.objects.filter(disciplina = fk)
        except Disciplinas.DoesNotExist:
            raise Http404
    
    def get(self, request, fk):
        disciplina = self.get_disciplina(fk)
        serializer = DisciplinasSerializer(disciplina, many = True)
        return Response(serializer.data)

class TemasListView(APIView):
    def get_tema(self, fk):
        try:
            return Temas.objects.filter(disciplina = fk)
        except Temas.DoesNotExist:
            raise Http404
    
    def get(self, request, fk):
        tema = self.get_tema(fk)
        serializer = TemasSerializer(tema, many = True)
        return Response(serializer.data)

class MapasTextoListView(APIView):
    def get(self, request):
        mapas = MapasTexto.objects.all()
        serializer = MapasTextosSerializer(mapas, many = True)
        return Response(serializer.data)

class AulasListView(APIView):
    def get_aulas(self, fk):
        try:
            return Aulas.objects.filter(tema = fk)
        except Aulas.DoesNotExist:
            raise Http404

    def get(self, request, fk):
        aulas = self.get_aulas(fk)
        serializer = AulasSerializer(aulas, many = True)
        return Response(serializer.data)

class AulasDetailView(APIView):
    def get_aulas(self, fk):
        try:
            return Aulas.objects.filter(disciplina = fk)
        except Aulas.DoesNotExist:
            raise Http404

    def get(self, request, fk):
        aulas = self.get_aulas(fk)
        serializer = AulasSerializer(aulas, many = True)
        return Response(serializer.data)

class AvaliacoesListView(APIView):
    def get_avaliacoes(self, fk):
        try:
            return Avaliacoe.objects.filter(aula = fk)
        except Avaliacoe.DoesNotExist:
            raise Http404

    def get(self, request, fk):
        avaliacoes = self.get_avaliacoes(fk)
        serializer = AvaliacoesSerializer(avaliacoes, many = True)
        return Response(serializer.data)
    
    def post(self, request):
        avaliacaoSerializer =  AvaliacoesSerializer(data = request.data)
        if avaliacaoSerializer.is_valid():
            avaliacaoSerializer.save()
            return Response(avaliacaoSerializer.data, status = status.HTTP_201_CREATED)
        
        return Response(avaliacaoSerializer.errors) 
