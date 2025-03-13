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