import random, csv

def plik_csv():
    adresIP = "172.30.2."
    lista = []

    for i in range(1,101):
        adres = adresIP + str(i)
        nazwa = "P" + str(i)
        lista.append([nazwa, adres])

    #newline="" zapobiega dodawaniu pustych wierszy
    with open("pc.csv", mode="w", newline="") as plik:
        writer = csv.writer(plik)
        writer.writerow(["pc_name", "ip"]) #Nagłówki
        writer.writerows(lista)

    #Odczytanie zapisanego pliku csv i wyświetlenie jego zawartości
    with open("pc.csv", mode="r", newline="") as plik:
        reader = csv.DictReader(plik)
        for wiersz in reader:
            print(wiersz)

if __name__ == '__main__':
    plik_csv()