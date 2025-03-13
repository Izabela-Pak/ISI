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