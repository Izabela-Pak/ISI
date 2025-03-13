def liczby():  
    tabela=[]

    for i in range(1,101):
        if (i%3 ==0 ) | (i%5 ==0):
            tabela.append(i)

    print(tabela)

if __name__ == '__main__':
    liczby()