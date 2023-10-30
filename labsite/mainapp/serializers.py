from rest_framework import serializers
from .models import Osoba, Stanowisko, Genders

class OsobaSerializer(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    imie = serializers.CharField(required=True)

    nazwisko = serializers.CharField(required=True)

    plec = serializers.CharField()

    data_dodania = serializers.models.DateTimeField(auto_now_add=True, editable = False)

    stanowisko = serializers.PrimaryKeyRelatedField(queryset=Stanowisko.objects.all())

    def create(self, validated_data):
        return Osoba.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.imie = validated_data.get('imie', instance.imie)
        instance.nazwisko = validated_data.get('nazwisko', instance.nazwisko)
        instance.plec = validated_data.get('plec', instance.plec)
        instance.data_dodania = validated_data.get('data_dodania', instance.data_dodania)
        instance.stanowisko = validated_data.get('stanowisko', instance.stanowisko)
        instance.save()
        return instance

class OsobaModelSerializer(serializers.ModelSerializer):
     class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'data_dodania', 'stanowisko']
        read_only_fields = ['id']
    
class StanowiskoModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stanowisko
        fields = ['id', 'nazwa', 'opis']