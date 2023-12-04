from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Osoba, Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoModelSerializer
from rest_framework.authentication import TokenAuthentication
from .BearerToken.BearerTokenAuthentication import BearerTokenAuthentication

# OSOBA
@api_view(['GET'])
def osoby(request):
    search_phrase = request.GET.get('search', None)  

    if search_phrase:
        osoby = Osoba.objects.filter(Q(imie__icontains=search_phrase) | Q(nazwisko__icontains=search_phrase))
    else:
        osoby = Osoba.objects.all()

    serializer = OsobaModelSerializer(osoby, many=True)
    return Response(serializer.data)


    

@api_view(['GET'])
def osoba_get(request, pk):
    try:
        osoba = Osoby.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(OsobaModelSerializer(osoba).data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_create(request):
    serializer = OsobaModelSerializer(data = request.data)
    if serializer.is_valid():
        serializer.save(wlasciciel=request.user)
        return Response(serializer.data)
    return Response(serializer.errors)



@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def osoba_update(request, pk):
     try:
         osoba = Osoby.objects.get(pk=pk)
     except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
     serializer = OsobaModelSerializer(osoba, data=request.data)
     if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

 
@api_view(['DELETE'])
@authentication_classes([BearerTokenAuthentication]) 
@permission_classes([IsAuthenticated])
def osoba_delete(request, pk): 
    try:
        osoba = Osoby.objects.get(pk=pk)
    except Osoba.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    osoba.delete()
    return Response(status=status.HTTP_204_NO_CONTENT) 

#STANOWISKO

@api_view(['GET'])
def stanowiska(request):
   
    stanowiska = Stanowisko.objects.all()

    serializer = StanowiskoModelSerializer(stanowiska, many=True)
    return Response(serializer.data)


    

@api_view(['GET'])
def stanowisko_get(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(StanowiskoModelSerializer(stanowisko).data)


@api_view(['POST'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_create(request):
    serializer = StanowiskoModelSerializer(data=request.data)

    if serializer.is_valid():
        # serializer.save(wlasciciel=request.user)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_update(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = StanowiskoModelSerializer(stanowisko, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@authentication_classes([SessionAuthentication, BasicAuthentication])
@permission_classes([IsAuthenticated])
def stanowisko_delete(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    stanowisko.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@authentication_classes([BearerTokenAuthentication]) 
@permission_classes([IsAuthenticated])
def stanowisko_members(request, pk):
    try:
        stanowisko = Stanowisko.objects.get(pk=pk)
        osoby = Osoba.objects.filter(stanowisko=stanowisko)
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)
    except Stanowisko.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)