from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
from django.db.models import Q
from .models import Osoba, Stanowisko
from .serializers import OsobaModelSerializer, StanowiskoModelSerializer

class OsobyList(APIView):
    def get(self, request):
        search_phrase = request.GET.get('search', None)
        if search_phrase:
            osoby = Osoba.objects.filter(Q(imie__icontains=search_phrase) | Q(nazwisko__icontains=search_phrase))
        else:
            osoby = Osoba.objects.all()
        serializer = OsobaModelSerializer(osoby, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OsobaModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OsobaDetail(APIView):
    def get_object(self, pk):
        try:
            return Osoba.objects.get(pk=pk)
        except Osoba.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        osoba = self.get_object(pk)
        serializer = OsobaModelSerializer(osoba)
        return Response(serializer.data)

    def put(self, request, pk):
        osoba = self.get_object(pk)
        serializer = OsobaModelSerializer(osoba, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        osoba = self.get_object(pk)
        osoba.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)






class StanowiskoList(APIView):
    def get(self, request):
        stanowiska = Stanowisko.objects.all()
        serializer = StanowiskoModelSerializer(stanowiska, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = StanowiskoModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StanowiskoDetail(APIView):
    def get_object(self, pk):
        try:
            return Stanowisko.objects.get(pk=pk)
        except Stanowisko.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        stanowisko = self.get_object(pk)
        serializer = StanowiskoModelSerializer(stanowisko)
        return Response(serializer.data)

    def put(self, request, pk):
        stanowisko = self.get_object(pk)
        serializer = StanowiskoModelSerializer(stanowisko, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        stanowisko = self.get_object(pk)
        stanowisko.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

