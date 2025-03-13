import random
import string

def hasla():
    #Utworzenie tablicy wygenerowanych losowo haseł
    slowa = [''.join(random.choices(string.ascii_letters + string.digits, k=6)) for _ in range(10000)]

    with open("password.txt", "w") as plik:
        for litera in slowa:
            plik.write(litera + "\n")

if __name__ == '__main__':
    hasla()