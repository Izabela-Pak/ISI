def liczby():
    count = 0
    for i in range(1, 101):
        if (i % 3 == 0) & (i % 4 == 0):
            print(i)
            count += 1
    print("Łączna ilość liczb podzielnych przez 3 i 4: ", count)

if __name__ == '__main__':
    liczby()