from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.http import Http404
from django.contrib.auth.models import User

class login(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        from django.db.models import Q
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        return Response({
            'user_id': user.pk,
        })

class cadastro(APIView):
    def post(self, request):
        username = request.data.get('username')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        email = request.data.get('email')
        senha = request.data.get('senha')
        escolaridade = request.data.get('escolaridade')
        vestibulares =  request.data.get('vestibulares')
        curso =  request.data.get('curso')
        universidade =  request.data.get('universidade')

        if (len(username.strip()) == 0 or len(email.strip()) == 0 
            or len(senha.strip()) == 0 or len(escolaridade.strip()) == 0
            or len(vestibulares.strip()) == 0 or len(curso.strip()) == 0
            or len(universidade.strip()) == 0 or len(first_name.strip()) == 0
            or len(last_name.strip()) == 0):
            return Response({"response":"Preencha todos os campos!"})
    
        user = User.objects.filter(username=username)

        if user.exists():
            return Response({"response":"Usuário já existente"})
        
        try: 
            user = User.objects.create_user(username = username,
                                            first_name = first_name,
                                            last_name = last_name,
                                            email=email,
                                            password=senha)                              
            user.save()

            usuario = User.objects.get(username = username)
            
            informacao = Informacoe.objects.create_user(usuario = usuario, escolaridade = escolaridade, vestibulares = vestibulares, curso = curso, universidade = universidade)

            informacao.save()
            
            avaliacaoSerializer =  InformacoesSerializer(data = {
                                                                "usuario":usuario.id,
                                                                "escolaridade":escolaridade,
                                                                "vestibulares":vestibulares,
                                                                "curso":curso,
                                                                "universidade":universidade
                                                                })

            if avaliacaoSerializer.is_valid():
                avaliacaoSerializer.save()  
                return Response(avaliacaoSerializer.data, status = status.HTTP_201_CREATED)

            return Response(avaliacaoSerializer.errors) 
        except:
            return Response(avaliacaoSerializer.errors) 

# Create your views here.
