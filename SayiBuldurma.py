import numpy as np
import random

hane = 3
minHane = 100
maxHane = 1000


def SetMinMaxHane():
    global hane
    global minHane
    global maxHane

    minHane = 10 ** (hane - 1)
    maxHane = (minHane * 10) - 1


def RastgeleBenzersizSayi():  # Rakamları benzersiz rastgele 3 haneli tam sayı üretir.
    global minHane
    global maxHane

    b = False
    r = 0
    while not b:
        r = random.randrange(minHane, maxHane)
        b = Benzersiz(r)
    return r

def dönütAl():
    while True:
            try:
                dönüt = int(input("Dönüt:"))


matrix = np.empty(shape=(9, 3), dtype='object')
print(matrix)
print(matrix[5, 1])

#Ana kod
while dönüt != 3:
    dönüt = dönütAl()
    if dönüt == 3:
        print("Sayınız: ")
        break

