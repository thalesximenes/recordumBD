from django.urls import path
from .views import *

app_name = 'usuarios'

urlpatterns = [
    path('cadastro/',
         cadastro.as_view(), 
         name='cadastro'),
    path('login/',
         login.as_view(), 
         name='disciplinas'),
]