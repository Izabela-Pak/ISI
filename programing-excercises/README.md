# TASK-01
``` def spr1(dane: str) -> str:
   if dane and isinstance(dane[0], str) and dane[0].isdigit():
      return True
   else:
      return False

def spr2(dane: str) -> str:
   if dane and dane[0].isdigit():
      return True
   else:
      return False

if __name__ == '__main__':
   dane = input("Podaj dowolny znak: ")
   
   if spr1(dane):
      print("Znak jest liczbą")
   else:
      print("Znak nie jest liczbą")

   if spr2(dane):
      print("Znak jest liczbą")
   else:
      print("Znak nie jest liczbą")
```

![Task-01](./screenshots/task-01.png)

[skrypt01-25101.py](./skrypt01-25101.py)

# TASK-02
```
def spr(dane: str) -> str:
    if len(dane) >= 2 and all(znak.isdigit() for znak in dane):
        return True
    else:
        return False

if __name__ == '__main__':
    dane = input("Podaj ciąg znaków ")
    if spr(dane):
        print("Ciąg jest liczbą")
    else:
        print("Ciąg nie jest liczbą")
```
![Task-02](./screenshots/task-02.png)

[skrypt02-25101.py](./skrypt02-25101.py)

# TASK-03
```
def szukanie():
    dane = "To jest długi ciąg znaków"
    #Wyszukjemy wpierw literę, potem wyraz, a na koniec coś czego nam nie znajdzie
    indeks1 = dane.find("z")
    indeks2 = dane.find("ciąg")
    indeks3 = dane.find("b")

    print(indeks1)
    print(indeks2)
    print(indeks3)

if __name__ == '__main__':
    szukanie()
```
![Task-03](./screenshots/task-03.png)

[skrypt03-25101.py](./skrypt03-25101.py)

# TASK-04
```
def szukanie(dane: str, szukana: str) -> str:
    lista_wyrazow = dane.split()
    indeksy = [i for i, wyraz in enumerate(lista_wyrazow) if wyraz == szukana]
    if not indeksy:
        indeksy = -1
    print(szukana)
    print(indeksy)

if __name__ == '__main__':
    dane = "banan jabłko gruszka borówki truskawki gruszka pomarańcza jabłko gruszka"
    szukana = "jabłko"
    szukanie(dane, szukana)
```
![Task-04](./screenshots/task-04.png)

[skrypt04-25101.py](./skrypt04-25101.py)

# TASK-05
```
import math
#Pierwszy sposób
def pierwszy_sposob():
    podzielne = [i for i in range(1, 257) if math.sqrt(i)%2==0 ]
    print (podzielne)

#Drugi sposób
def drugi_sposob():
    podzielne2 = []
    for i in range(1,257):
        if math.sqrt(i) % 2 ==0:
            podzielne2.append(i)
    print(podzielne2)

if __name__ == '__main__':
    pierwszy_sposob()
    drugi_sposob()
```
![Task-05](./screenshots/task-05.png)

[skrypt05-25101.py](./skrypt05-25101.py)

# TASK-06
```
import string
import random

# Tworzenie słownika z nazwą zawierającą numer albumu
def slownik(nazwa: str) -> str:
    slownik = {i: ''.join(random.choices(string.ascii_letters + string.digits, k=8)) for i in range(10, 21)}

    # Wyświetlenie słownika
    print(nazwa, "=", slownik)

if __name__ == '__main__':
    nazwa_slownika = "25101"
    slownik(nazwa_slownika)
```
![Task-06](./screenshots/task-06.png)

[skrypt06-25101.py](./skrypt06-25101.py)

# TASK-07
```
import sys
sys.path.append("utils")
import obliczenia


if __name__ == '__main__':
    obliczenia.pierwiastek(25)
    obliczenia.sin_cos(90)
    obliczenia.odległosc_euklidesowa([-1,4], [1,2])
    obliczenia.logarytm(5,10)
```
![Task-07](./screenshots/task-07.png)

[skrypt07-25101.py](./skrypt07-25101.py)

# TASK-08
```
import random
import string
from collections import Counter

def zad():
    lancuch = random.choices(string.ascii_letters, k=100)
    slownik = Counter(lancuch)
    lista = list(slownik.items())

    print(lista)

if __name__ == '__main__':
    zad()
```
![Task-08](./screenshots/task-08.png)

[skrypt08-25101.py](./skrypt08-25101.py)

# TASK-09
```
from datetime import datetime

class Vehicle:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.przebieg = przebieg
        self.rok_produkcji = rok_produkcji

    @property
    def wiek(self):
        return datetime.now().year - self.rok_produkcji
    
    def is_old(self):
        return self.wiek > 10
    
    def is_long_mileage(self):
        return self.przebieg > 200_000


class Car:
    def __init__(self, nazwa, rok_produkcji, przebieg):
        self.nazwa = nazwa
        self.przebieg = przebieg
        self.rok_produkcji = rok_produkcji

    @property
    def wiek(self):
        return datetime.now().year - self.rok_produkcji
    
    def is_old(self):
        return self.wiek > 15
    
    def is_long_mileage(self):
        return self.przebieg > 250_000
    
class CarAfterVehicle(Vehicle):
    def __init__(self, nazwa, rok_produkcji, przebieg):
        super().__init__(nazwa, rok_produkcji, przebieg)  # Wywołanie konstruktora Vehicle


if __name__ == '__main__':
    vehicle = Vehicle("BMW", 2013, 150_000)
    car = Car("Tesla", 2020, 201_000)
    dziedziczenie = CarAfterVehicle("Fiat", 2009, 300_000)

    print("Auto z klasy Vehicle")
    print("Wiek pojazdu:", vehicle.wiek)
    print("Czy jest stary?", vehicle.is_old())
    print("Czy ma duży przebieg?", vehicle.is_long_mileage())

    print("Auto z klasy Car")
    print("Wiek pojazdu:", car.wiek)
    print("Czy jest stary?", car.is_old())
    print("Czy ma duży przebieg?", car.is_long_mileage())

    print("Auto z klasy dziedziczącej po Vehicle")
    print("Wiek pojazdu:", dziedziczenie.wiek)
    print("Czy jest stary?", dziedziczenie.is_old())
    print("Czy ma duży przebieg?", dziedziczenie.is_long_mileage())
```
![Task-09](./screenshots/task-09.png)

[skrypt09-25101.py](./skrypt09-25101.py)

# TASK-10
```
def zapis_plik():
    lancuch = ""
    for i in range(97, 123):
        lancuch += chr(i)

    # "w" oznacza tryb zapisu. Jeśli plik już istnieje to go nadpisze
    with open("alfabet1-25101.txt", "w") as plik:
        plik.write(lancuch)

    with open("alfabet2-25101.txt", "w") as plik:
        for litera in lancuch:
            plik.write(litera + "\n")


if __name__ == '__main__':
    zapis_plik()
```
![Task-10-1](./screenshots/task-10-1.png)

![Task-10-2](./screenshots/task-10-2.png)

[skrypt10-25101.py](./skrypt10-25101.py)

# TASK-11
```
def odwrocenie(text: str) -> str:
    odwrocona_sentencja = text[::-1]
    print(odwrocona_sentencja)


if __name__ == '__main__':
    sentencja = input("Podaj sentencję: ")
    odwrocenie(sentencja)
```
![Task-11](./screenshots/task-11.png)

[skrypt11-25101.py](./skrypt11-25101.py)

# TASK-12
```
def zamiana(sentencja:str) -> str:
    zmiana1 = sentencja.replace("o","0")
    zmiana2 = zmiana1.replace("e","3")
    zmiana3 = zmiana2.replace("i","1")
    nowa_sentencja = zmiana3.replace("a","4")

    print(nowa_sentencja)

if __name__ == '__main__':
    sentencja = input("Podaj sentencję: ")
    zamiana(sentencja)
```
![Task-12](./screenshots/task-12.png)

[skrypt12-25101.py](./skrypt12-25101.py)

# TASK-13
```
def liczby():
    for i in range(1,51):
        if i%3 != 0:
            print(i)

if __name__ == '__main__':
    liczby()
```
![Task-13](./screenshots/task-13.png)

[skrypt13-25101.py](./skrypt13-25101.py)

# TASK-14
```
def liczby():
    count = 0
    for i in range(1, 101):
        if (i % 3 == 0) & (i % 4 == 0):
            print(i)
            count += 1
    print("Łączna ilość liczb podzielnych przez 3 i 4: ", count)

if __name__ == '__main__':
    liczby()
```
![Task-14](./screenshots/task-14.png)

[skrypt14-25101.py](./skrypt14-25101.py)
# TASK-15
```
def liczby():  
    tabela=[]

    for i in range(1,101):
        if (i%3 ==0 ) | (i%5 ==0):
            tabela.append(i)

    print(tabela)

if __name__ == '__main__':
    liczby()
```
![Task-15](./screenshots/task-15.png)

[skrypt15-25101.py](./skrypt15-25101.py)
