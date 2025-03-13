# TASK-01
` def spr1(dane: str) -> str:
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
      print("Znak nie jest liczbą") `

[Task-01](./screenshots/task-01.png)
[skrypt01-25101.py](./skrypt01-25101.py)

TASK-02
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

[Task-02](./screenshots/task-02.png)
[skrypt02-25101.py](./skrypt02-25101.py)

TASK-03
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

[Task-03](./screenshots/task-03.png)
[skrypt03-25101.py](./skrypt03-25101.py)

TASK-04
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

[Task-04](./screenshots/task-04.png)
[skrypt04-25101.py](./skrypt04-25101.py)

TASK-05
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

[Task-05](./screenshots/task-05.png)
[skrypt05-25101.py](./skrypt05-25101.py)

TASK-06
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

[Task-06](./screenshots/task-06.png)
[skrypt06-25101.py](./skrypt06-25101.py)

TASK-07
import sys
sys.path.append("utils")
import obliczenia


if __name__ == '__main__':
    obliczenia.pierwiastek(25)
    obliczenia.sin_cos(90)
    obliczenia.odległosc_euklidesowa([-1,4], [1,2])
    obliczenia.logarytm(5,10)

[Task-07](./screenshots/task-07.png)
[skrypt07-25101.py](./skrypt07-25101.py)

