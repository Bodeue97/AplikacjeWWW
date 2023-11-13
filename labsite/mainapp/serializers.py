from rest_framework import serializers
from .models import Osoba, Stanowisko, Genders


        

class OsobaModelSerializer(serializers.ModelSerializer):

    
   def validate_imie(self, value):
      if not value.isalpha():
         raise serializers.ValidationError("Imie ma skladac sie tylko z liter.")
      return value
         

   # def validate_nazwisko(self, value):
   #    if not value.replace(" ", "").isalpha():
   #       raise serializers.ValidationError("Nazwisko ma skladac sie tylko z liter.")
 

   def validate_data_dodania(self, value):
        if value > timezone.now():
            raise serializers.ValidationError("Data dodania nie moze byc w przyszlosci")
        return value

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

   class Meta:
        model = Osoba
        fields = ['id', 'imie', 'nazwisko', 'plec', 'data_dodania', 'stanowisko']
        read_only_fields = ['id']
    
class StanowiskoModelSerializer(serializers.ModelSerializer):
   def create(self, validated_data):
      return Stanowisko.objects.create(**validated_data)
   def update(self, instance, validated_data):
      instance.nazwa = validated_data.get('nazwa', instance.nazwa)
      instance.opis = validated_data.get('opis', instance.opis)
      instance.save()
      return instance


   class Meta:
        model = Stanowisko
        fields = ['id', 'nazwa', 'opis']