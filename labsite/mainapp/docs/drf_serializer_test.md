# Serializacja stanowisko
import io
from mainapp.models import Osoba, Stanowisko, Genders
from mainapp.serializers import OsobaSerializer, OsobaModelSerializer, StanowiskoModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
stanowisko = Stanowisko(nazwa='Żongler', opis='Żongluje jak mu przykro')
stanowisko.save()
stanowiskoSerializer = StanowiskoModelSerializer(stanowisko)
stanowiskoSerializer.data
contentStanowisko = JSONRenderer().render(stanowiskoSerializer.data)
contentStanowisko

# Serializacja osoba

osoba = Osoba(imie='Andrzej', nazwisko='Andrzejewski', plec=Genders.MALE, stanowisko=stanowisko)
osoba.save()
osobaSerializer = OsobaSerializer(osoba)
osobaSerializer.data
contentOsoba = JSONRenderer().render(osobaSerializer.data)
contentOsoba

# Deserializacja stanowisko

streamStanowisko = io.BytesIO(contentStanowisko)
dataStanowisko = JSONParser().parse(streamStanowisko)
stanowiskoDeserializer = StanowiskoModelSerializer(data=dataStanowisko)
stanowiskoDeserializer.is_valid()
stanowiskoDeserializer.errors
repr(stanowiskoDeserializer)
stanowiskoDeserializer.save()
stanowiskoDeserializer.data

# Deserializacja osoba

streamOsoba = io.BytesIO(contentOsoba)
dataOsoba = JSONParser().parse(streamOsoba)
osobaDeserializer = OsobaSerializer(data=dataOsoba)
osobaDeserializer.is_valid()
osobaDeserializer.errors
repr(osobaDeserializer)
osobaDeserializer.save()
osobaDeserializer.data










