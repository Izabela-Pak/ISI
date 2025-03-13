
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