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