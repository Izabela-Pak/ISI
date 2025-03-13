def odwrocenie(text: str) -> str:
    odwrocona_sentencja = text[::-1]
    print(odwrocona_sentencja)


if __name__ == '__main__':
    sentencja = input("Podaj sentencję: ")
    odwrocenie(sentencja)