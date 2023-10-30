1. wyświetl wszystkie obiekty modelu Osoba

from mainapp.models import Osoba
osoba_objects = Osoba.objects.all()
for osoba in osoba_objects:
    print(f'{osoba}')

2. wyświetl obiekt modelu Osoba z id = 3

from mainapp.models import Osoba
osoba_objects = Osoba.objects.all()
for osoba in osoba_objects:
    if(osoba.id == 3):  
        print(f'{osoba}')
3. wyświetl obiekty modelu Osoba, których nazwa rozpoczyna się na wybraną przez Ciebie literę alfabetu (tak, żeby był co najmniej jeden wynik)

from mainapp.models import Osoba
osoba_objects = Osoba.objects.all()
for osoba in osoba_objects:
    if(osoba.imie[0] == 'A'):  
        print(f'{osoba}')
4. wyświetl unikalną listę stanowisk przypisanych dla modeli Osoba

from mainapp.models import Osoba

distinct_stanowiska = set()
osoba_objects = Osoba.objects.all()
for osoba in osoba_objects:
    distinct_stanowiska.add(osoba.stanowisko)
for stanowisko in distinct_stanowiska:
    print(stanowisko)


5. wyświetl nazwy stanowisk posortowane alfabetycznie malejąco

from mainapp.models import Stanowisko
stanowiska = Stanowisko.objects.all().order_by('-nazwa')
for stanowisko in stanowiska:
    print(stanowisko)

6. dodaj nową instancję obiektu klasy Osoba i zapisz w bazie.

from mainapp.models import Osoba, Stanowisko
stanowiska = Stanowisko.objects.all()
new_osoba = Osoba(imie ='Andrzej', nazwisko ='Andrzejewski', stanowisko=stanowiska[0], plec = 1)
new_osoba.save()







    