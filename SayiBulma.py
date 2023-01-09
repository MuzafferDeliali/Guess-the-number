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


def Benzersiz(x):  # Bir tam sayının rakamları benzersiz ise True, değilse False döndürür.
    s = str(x)  # Sayının string karşılığı
    n = len(s)  # Sayının karakter uzunluğu (hane sayısı)
    for i in range(n-1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                return False
    return True


def HaneSayiAl():

    while True:
        try:
            h = int(input("Hane: "))
        except:
            h = 0

        if 3 <= h <= 5:
            return h
        else:
            print("3-5 arası hane sayısı belirtiniz!")


def RastgeleBenzersizSayi():  # Rakamları benzersiz rastgele 3 haneli tam sayı üretir.
    global minHane
    global maxHane

    b = False
    r = 0
    while not b:
        r = random.randrange(minHane, maxHane)
        b = Benzersiz(r)
    return r


def Karsilastir(sayi1, sayi2):
    s1 = str(sayi1)
    s2 = str(sayi2)

    arti = 0
    eksi = 0
    for i in range(len(s1)):
        for j in range(len(s2)):
            if s1[i] == s2[j]:
                if i == j:
                    arti = arti + 1
                else:
                    eksi = eksi + 1
    if arti == 0 and eksi == 0:
        return "0"
    else:
        sonuc = ""
        if arti > 0:
            sonuc = sonuc + "+" + str(arti)

        if eksi > 0:
            sonuc = sonuc + "-" + str(eksi)

        return sonuc


def TahminAl():
    global hane
    global minHane
    global maxHane
    while True:
        try:
            tahmin = int(input("Tahmin:"))
        except:
            tahmin = 0

        b = Benzersiz(tahmin)
        if b and minHane < tahmin < maxHane:
            return tahmin
        else:
            print(str(hane) + " haneli rakamları benzersiz bir tahminde bulunun!")


# ANA PROGRAM BURADAN BAŞLIYOR
print("Sayi bulma oyununa hoş geldiniz")
print('1. Oyna')
print('2. Cık')

print('Oynamak ister misin?')
textInput = str(input())

while textInput != 2:
    if textInput == 1:
        print("SAYI BULMA OYUNU")
        hane = HaneSayiAl()
        kazanskor = "+" + str(hane)
        SetMinMaxHane()
        print(str(hane) + " haneli bir sayı tuttum. Bil bakalım.")
        sayi = RastgeleBenzersizSayi()

        sonuc = ""

        while sonuc != kazanskor:
            tahmin = TahminAl()
            sonuc = Karsilastir(tahmin, sayi)
            print(sonuc)
            if sonuc == kazanskor:
                print("TEBRİKLER BİLDİNİZ.")
                print("")
                print('Oynamak ister misin?')
                print('1. Oyna')
                print('2. Cık')
                textInput = int(input())

    elif textInput == 2:
        print("Teşekkürler")

    else:
        print("nE?")
        break
