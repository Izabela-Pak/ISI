def palindrom(dane:str) -> str:
    check_dane = dane.replace(" ", "")
    odwrocone = check_dane[::-1]

    if(check_dane==odwrocone):
        print("Wyraz/zdanie jest palindromem")
    else:
        print("Wyraz/zdanie nie jest palindromem")

if __name__ == '__main__':
    dane = input("Podaj wyraz lub zdanie: ")
    palindrom(dane)