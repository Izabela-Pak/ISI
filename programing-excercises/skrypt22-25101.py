def max_word(words):
    max_length=""
    for slowo in words:
        if len(max_length) < len(slowo):
            max_length = slowo
    return max_length

def ten_length(words):
    same_len= []
    for slowo in words:
        if len(slowo)==10:
            same_len.append(slowo)
    return same_len

def spr_pliku():
    with open("wordlist_10000.txt", "r") as plik:
        linie = plik.readlines()
    max = max_word(linie)
    ten_len = ten_length(linie)

    print(max)
    print(ten_len)

if __name__ == '__main__':
    spr_pliku()