import io
from mainapp.models import Osoba, Stanowisko
from mainapp.serializers import OsobaSerializer, OsobaModelSerializer, StanowiskoModelSerializer
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
stanowisko = Stanowisko(nazwa='Żongler', opis='Żongluje jak mu przykro')
stanowisko.save()
stanowiskoSerializer = StanowiskoModelSerializer(stanowisko)
stanowiskoSerializer.data
contentStanowisko = JSONRenderer().render(stanowiskoSerializer.data)
contentStanowisko
osoba = Osoba(imie='Andrzej', nazwisko='Andrzejewski', plec=Genders(1), stanowisko=stanowisko)
osoba.save()
osobaSerializer = OsobaSerializer(osoba)
osobaSerializer.data
contentOsoba = JSONRenderer().render(osobaSerializer.data)
contentOsoba
streamStanowisko = io.BytesIO(contentStanowisko)
dataStanowisko = JSONParser().parse(streamStanowisko)
stanowiskoDeserializer = StanowiskoModelSerializer(data=dataStanowisko)
stanowiskoDeserializer.is_valid()
stanowiskoDeserializer.errors
repr(stanowiskoDeserializer)

