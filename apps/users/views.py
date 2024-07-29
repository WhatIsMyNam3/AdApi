from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED, HTTP_400_BAD_REQUEST,
    HTTP_404_NOT_FOUND
)

from .serializers import LoginSerializer, RegisterSerializer
from rest_framework.authtoken.models import Token


@api_view(['POST'])
def login(request):
    user = get_object_or_404(User, username=request.data['username'])
    if not user.check_password(request.data['password']):
        return Response({'detail': 'Not found'}, status=HTTP_404_NOT_FOUND)
    token, created = Token.objects.get_or_create(user=user)
    serializer = LoginSerializer(user)
    return Response({'token': token.key, 'user': serializer.data})


@api_view(['POST'])
def signup(request):
    serializer = RegisterSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        user = User.objects.get(username=request.data['username'])
        user.set_password(request.data['password'])
        user.save()
        token = Token.objects.create(user=user)
        return Response(
            {'token': token.key, 'user': serializer.data},
            status=HTTP_201_CREATED
        )
    return Response({serializer.errors}, status=HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def token(request):
    return Response({})
