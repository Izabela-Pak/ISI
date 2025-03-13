import math
#Pierwszy sposób
def pierwszy_sposob():
    podzielne = [i for i in range(1, 257) if math.sqrt(i)%2==0 ]
    print (podzielne)

#Drugi sposób
def drugi_sposob():
    podzielne2 = []
    for i in range(1,257):
        if math.sqrt(i) % 2 ==0:
            podzielne2.append(i)
    print(podzielne2)

if __name__ == '__main__':
    pierwszy_sposob()
    drugi_sposob()