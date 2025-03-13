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