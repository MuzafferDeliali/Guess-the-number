import random


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
            hane = int(input("Hane: "))
        except:
            hane = 0

        if 0 < hane < 6:
            return hane
        else:
            print("0-6 arası hane sayısı belirt!")

def RastgeleBenzersizSayi(hane):  # Rakamları benzersiz rastgele 3 haneli tam sayı üretir.
    b = False
    r = 0
    while not b:
        minHane = 10 ** (hane - 1)
        maxHane = (minHane * 10) - 1
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
    while True:
        try:
            tahmin = int(input("Tahmin:"))
        except:
            tahmin = 0

        b = Benzersiz(tahmin)
        if b and minHane < tahmin < maxHane:
            return tahmin
        else:
            print("3 haneli rakamları benzersiz bir tahminde bulunun!")


# ANA PROGRAM BURADAN BAŞLIYOR
print("SAYI BULMA OYUNU")
print("3 haneli bir sayı tuttum. Bil bakalım.")
sayi = RastgeleBenzersizSayi(HaneSayiAl())

sonuc = ""
while sonuc != "+3":
    tahmin = TahminAl()
    sonuc = Karsilastir(tahmin, sayi)
    print(sonuc)
    if sonuc == "+3":
        print("TEBRİKLER BİLDİNİZ.")
