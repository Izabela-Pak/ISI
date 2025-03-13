def spr(dane: str) -> str:
    if len(dane) >= 2 and all(znak.isdigit() for znak in dane):
        return True
    else:
        return False

if __name__ == '__main__':
    dane = input("Podaj ciąg znaków ")
    if spr(dane):
        print("Ciąg jest liczbą")
    else:
        print("Ciąg nie jest liczbą")