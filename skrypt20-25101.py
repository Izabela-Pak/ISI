import random

def gra():
    liczba = random.randint(1,100)

    while True:
        podana_liczba = int(input("Podaj liczbę z przedziału od 1 do 100: "))

        if podana_liczba == liczba:
            print("Gratulację! Udało Ci się zgadnąć!")
            break
        elif podana_liczba < liczba:
            print("Podana liczba jest za mała! Spróbuj ponownie")
        else:
            print("Podana liczba jest za duża! Spróbuj ponownie")

if __name__ == '__main__':
    gra()