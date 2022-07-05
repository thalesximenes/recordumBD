from django.urls import path, include
from .views import *

app_name = 'disciplinas'

urlpatterns = [
    path('eixos/',
         EixosListView.as_view(), 
         name='eixos list'),

    path('disciplinas/',
         DisciplinasListView.as_view(), 
         name='disciplinas list'),

    path('disciplinas/<int:fk>',
         DisciplinasDetailView.as_view(), 
         name='disciplinas detail'),

    path('disciplinas/<int:fk>/temas',
         TemasListView.as_view(), 
         name='temas list'),
    
    path('aulas/temas/<int:fk>',
         AulasListView.as_view(), 
         name='aulas list temas'),

     path('aulas/disciplina/<int:fk>',
         AulasDetailView.as_view(), 
         name='aulas list disciplina'),

    path('avaliacoes/<int:fk>',
         AvaliacoesListView.as_view(), 
         name='avaliacoes'),

    path('mapastexto/',
         MapasTextoListView.as_view(), 
         name='mapastexto'),

    # path('arquivos/recuperar/<int:pk>/',
    #     arquivos_recuperar, 
    #     name='arquivos_recuperar'),

]
