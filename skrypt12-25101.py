def zamiana(sentencja:str) -> str:
    zmiana1 = sentencja.replace("o","0")
    zmiana2 = zmiana1.replace("e","3")
    zmiana3 = zmiana2.replace("i","1")
    nowa_sentencja = zmiana3.replace("a","4")

    print(nowa_sentencja)

if __name__ == '__main__':
    sentencja = input("Podaj sentencję: ")
    zamiana(sentencja)