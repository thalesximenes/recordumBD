from django.urls import path, include
from .views import *

app_name = 'disciplinas'

urlpatterns = [
    path('eixos/',
         EixosListView.as_view(), 
         name='eixos'),

    path('disciplinas/',
         DisciplinasListView.as_view(), 
         name='disciplinas'),

    path('disciplinas/<int:fk>',
         DisciplinasDetailView.as_view(), 
         name='disciplinas'),

    path('mapastexto/',
         MapasTextoListView.as_view(), 
         name='mapastexto'),

    path('aulas/<int:fk>',
         AulasListView.as_view(), 
         name='aulas'),

    path('aulas/<int:fk>/<str:tema>',
         TemasListView.as_view(), 
         name='aulas'),
    
    path('avaliacoes/<int:fk>',
         AvaliacoesListView.as_view(), 
         name='avaliacoes'),

    # path('arquivos/recuperar/<int:pk>/',
    #     arquivos_recuperar, 
    #     name='arquivos_recuperar'),

]
