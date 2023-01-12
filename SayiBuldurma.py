import random
import numpy as np
hane = 3
minHane = 100
maxHane = 1000

ihtimal = np.full((10, 3), 1, dtype=int)
ihtimal[0][0] = 0
tahminler = np.empty((1, 3), int)


def ConvInt(val, d):
    try:
        return int(val)
    except:
        return d


def ResetIhtimal():
    global ihtimal
    for r in range(10):
        for c in range(3):
            ihtimal[r][c] = 1
    ihtimal[0][0] = 0


def SetMinMaxHane():
    global hane, minHane, maxHane

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
        h = ConvInt(input("Hane: "), 0)
        if 3 <= h <= 5:
            return h
        else:
            print("3-5 arası hane sayısı belirtiniz!")


def RastgeleBenzersizSayi():  # Rakamları benzersiz rastgele 3 haneli tam sayı üretir.
    global minHane, maxHane
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


def SonucDogrulama(sonuc):
    global hane
    if len(sonuc) == 1:
        return sonuc == "0"
    elif len(sonuc) == 2:
        if sonuc[0] != "-" and sonuc[0] != "+":
            return False
        d = ConvInt(sonuc[1], 0)
        if d < 1 or d > hane:
            return False
        return True

    elif len(sonuc) == 4:
        if sonuc[0] != "+" or sonuc[2] != "-":
            return False

        d1 = ConvInt(sonuc[1], 0)
        if d1 < 1 or d1 >= hane:
            return False

        d2 = ConvInt(sonuc[3], 0)
        if d2 < 1 or d2 >= hane:
            return False

        if d1 + d2 > hane:
            return False

        return True


def GetArti(sonuc):
    if sonuc[0] == "-" or sonuc[0] == "0":
        return 0
    else:
        return ConvInt(sonuc[1], 0)


def GetEksi(sonuc):
    if sonuc[0] == "-":
        return ConvInt(sonuc[1], 0)
    else:
        if len(sonuc) == 4:
            return ConvInt(sonuc[1], 0)
        else:
            return 0


def GetSifirIhtimalAdet(tahmin):
    global ihtimal
    adet = 0
    s_tahmin = str(tahmin)
    for c in range(len(s_tahmin)):
        r = int(s_tahmin[c])
        if np.all((ihtimal[r] == [0] * hane)):
            adet = adet + 1
    return adet


def GecmisIslem():
    global hane
    for i in range(len(tahminler)):
        if tahminler[i][1] > 0 and tahminler[i][2] == 0:  # Sonucu sadece artı olan tahmin ise
            tahmin = tahminler[i][0]
            sifir = GetSifirIhtimalAdet(tahmin)
            if sifir + tahminler[i][1] == hane:  # Sıfırlar ve artıların toplamı hane kadar ise artıların yeri kesindir.
                s_tahmin = str(tahmin)
                for c in range(len(s_tahmin)):
                    r = int(s_tahmin[c])
                    if ihtimal[r][c] > 0:
                        ihtimal[:, c] = 0
                        ihtimal[r][c] = 2


def SonucIslem(tahmin, sonuc):
    global hane, ihtimal, tahminler
    arti = GetArti(sonuc)
    eksi = GetEksi(sonuc)
    tahminler = np.append(tahminler, np.array([[tahmin, arti, eksi]]), axis=0)
    s_tahmin = str(tahmin)
    for c in range(len(s_tahmin)):
        r = int(s_tahmin[c])
        if arti == 0 and eksi == 0:  # Hiçbir rakam tutmadı
            ihtimal[r] = [0] * hane
        elif arti == 0:  # Tutan rakamların hiçbiri yerinde değil (Sadece Eksi)
            ihtimal[r][c] = 0

    if arti + eksi == hane:  # arti ve eksi toplami haneye eşit (tahmin dışındaki rakamları sıfırla)
        for r in range(10):
            if s_tahmin.find(str(r)) == - 1:
                for c in range(hane):
                    ihtimal[r][c] = 0
    GecmisIslem()


def TahminYap():
    global ihtimal
    while True:
        s_tahmin = ""
        for c in range(hane):
            rlist = []
            for r in range(10):
                i = ihtimal[r][c]
                if i != 0:
                    rlist.append(r)
            ind = random.randrange(0, len(rlist))
            s_tahmin = s_tahmin + str(rlist[ind])
        tahmin = int(s_tahmin)
        if Benzersiz(tahmin) and tahmin not in tahminler[:, 0]:
            return tahmin


def SonucAl():
    while True:
        sonuc = str(input("Sonuç:"))
        dogrumu = SonucDogrulama(sonuc)
        if dogrumu:
            return sonuc
        else:
            print("Girdiğiniz sonuç geçerli değil!")


def DevamOnayiAl():
    while True:
        cevap = input("Tekrar oynamak ister misiniz(E/H) ? ")
        if cevap == "E" or cevap == "e":
            return True
        elif cevap == "H" or cevap == "h":
            return False
        else:
            print("Cevap anlaşılamadı. E veya H olarak cevaplayın.")


def OyunOyna():
    global hane
    hane = HaneSayiAl()
    kazanskor = "+" + str(hane)
    print(str(hane) + " haneli bir sayı tut, Ben bilmeye çalışayım.")
    sonuc = ""

    while sonuc != kazanskor:
        tahmin = TahminYap()
        print(str(tahmin))
        sonuc = SonucAl()
        if sonuc == kazanskor:
            print("TUTTUĞUN SAYIYI BİLDİM.")
        else:
            SonucIslem(tahmin, sonuc)


# ANA PROGRAM BURADAN BAŞLIYOR
print("SAYI BULMA OYUNU")
tekraroyna = True
while tekraroyna:
    ResetIhtimal()
    OyunOyna()
    tekraroyna = DevamOnayiAl()
print("Bizimle oynadığınız için teşekkür ederiz.")
print(tahminler)
# print(d_sayilar)
print(ihtimal)
