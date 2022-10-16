# -*- coding: utf-8 -*-
"""
Gedik Üniversitesi
Veri Bilimi ve Makine Öğrenmesi

0001 
Giriş Dersleri
Temel Konular - Python 
"""

print("Hello world")

# Değişken atama yöntemleri
########################################################

print("# Değişken atama yöntemleri")
print("########################################################")

x = 8
ülke = "türKiye CUMhuriyeti"
nüfus = 80000000
kabul = True
digerUlke = "Finlandiya"
y = 9
z = 5.43
complexNum = 1j
excerpt = "LoreM ipSUm dOlor SiT AmEt teSt dEnEMe"
longText = """Gedik Üniversitesi
Python ile Veri Bilimi ve Makine Öğrenmesi
Temel Konular."""

a,b,c = 3,5,9

mavi = yeşil = kırmızı = "renk"

# Maths
########################################################

print("# Maths")
print("########################################################")

print("üs alma : ", 2 ** 3)
print("mod - kalan operatörü : ", 8 % 3)
print("tam sayılı bölme operatörü : ", 9 // 2)

print("İçinde var mı : ", "T" in ülke)
print("İçinde var mı : ", "t" in ülke)
print("İçinde yok mu : ", "h" not in ülke)

print(type(ülke))
print(type(complexNum))

# Listeler ve farklı tipler
########################################################

print("# Listeler ve farklı tipler")
print("########################################################")

colorList       = ["kırmızı", "sarı", "yeşil", "mavi"]
flowerTuple     = ("gül", "karanfil", "papatya", "gerbera")
locationDict    = {"ülke": "Türkiye", "başkent": "Ankara"}
meyveSets       = {"elma", "karpuz", "muz"}
baytData        = b"Merhaba"
baytArr         = bytearray(5)
memView         = memoryview(bytes(5))

print(colorList[0])
print(flowerTuple[0])
print(locationDict["ülke"])

multilevelList = ["ilk", "ikinci", "üçüncü", colorList]
print(multilevelList, len(multilevelList))
print(multilevelList[3][2])

# Slice işlemleri
########################################################

print("# Slice işlemleri")
print("########################################################")

print(colorList[0:2])
print(colorList[:3])
print(colorList[2:])

# Karakter İşlevleri
########################################################

print("# Karakter İşlevleri")
print("########################################################")

print("İlk harfi büyüt : ", ülke.capitalize())
print("İlk harfi küçült : ", ülke.casefold())
print("Büyük-Küçük tersine : ", excerpt.swapcase())
print("Harf büyüt : ", excerpt.upper())
print("Baş harfleri büyüt : ", excerpt.title())

print("Yazıyı 40 harfe tamamla ve yanları doldur : ", ülke.center(40, "#"))
print("Sayıyı 5 haneye tamamla ve önüne sıfır doldur : ", "99".zfill(5))

print("Python kaç kere geçiyor? : ", longText.count("Python"))
print("Nokta ile bitiyor mu? : ", longText.endswith("."))

print("Bul : ", longText.find("Üniversitesi"))      # varlığından emin değilsen ve sadece stringse
print("Index : ", longText.index("Üniversitesi"))   # varlığından eminsen ve string, lists, tuples.

# rfind, rindex : aranan ifadenin son geçtiği yer

breadTxt = "Ekmek sadece {fiyat:.2f} Türk Lirası"
print(breadTxt.format(fiyat = 4.5))

thisLocationTxt = "Burası {ulke_adi} olarak bilinmektedir. Nüfusu {toplam_nufus}".format(ulke_adi = ülke, toplam_nufus = nüfus)
print(thisLocationTxt)

myNameisTxt = "Adım {0} ve {1}".format("Uğur", 1989)
print(myNameisTxt)

weatherTxt = "Saat {} ve hava {} derece".format("23:15", 21)
print(weatherTxt)

print("Buraya biraz yazı ekliyorum".isalnum())      # False
print("23456".isalnum())                            # True

print("Burasıtamamenharfler".isalpha())     # True
print("Burası tamamen harfler".isalpha())   # False

print(" <3 ".join(flowerTuple))

print("       Range Rover      ".lstrip())

newLangTxt = longText.maketrans("ğĞüÜşŞİıöÖçÇ", "gGuUsSIioOcC")
print(longText.translate(newLangTxt))

print(excerpt.partition("SiT"))

print("Metin değiştirildi : ", longText.replace("Python", "GoLang"))

print(longText.splitlines())

print("Uygulanabilecek işlev listesi : ", dir(ülke))

# Fonksiyonlar
########################################################

print("# Fonksiyonlar")
print("########################################################")

def mutlakFark(x, y):
    return("mutlakFark : " + str(abs(x - y)))
    
print(mutlakFark(4, 6))

print(mutlakFark(y = 4, x = 9))

# Modüller
########################################################

print("# Modüller")
print("########################################################")

import random
print("İki sayı arasında rastgele bir sayı üret : ", random.randrange(0, 100)) # randint
print("Yerine koymadan (birbirinden farklı) birkaç tane sayı üret : ", random.sample(range(0, 10), 10))
print("Yerine koyup birkaç tane sayı üret : ", random.choices(range(0, 10), k = 10))
print("İki sayı arasında 2'şer atlayıp rastgele bir sayı üret : ", random.randrange(2, 100, 2)) 

# Python'da Döngüler ve Statistics Başlangıç
########################################################

print("# Python'da Döngüler ve Statistics Başlangıç")
print("########################################################")

for i in colorList:
    print(i)
    

import statistics # dir(statistics)
    
scores = random.choices(range(0,101), k = 60)
scores.sort()
scoreMean = statistics.mean(scores)
deviations = []
print("Mean of scores : ", scoreMean)

print("########################################################")

# Deviation from the mean
scoreKey = 0
for scoreKey, scoreVal in enumerate(scores, start = 0):
    currentDeviation = scoreVal - scoreMean
    deviations.append(currentDeviation)
    print(scoreKey, " - ", currentDeviation)

print('there were {0} items printed'.format(scoreKey + 1))

print('Standart sapmanın ortalaması : ', statistics.mean(deviations))

print("########################################################")

import itertools
nullDeviations = list(itertools.repeat(0, 60))

for loop in range(0, 60):
    nullDeviations[loop] = scores[loop] - statistics.mean(scores)
    
print("Appendsiz ekleme : ", statistics.mean(nullDeviations))

def celsius(fahrenheit):
    longDecCel = (fahrenheit - 32) / (9/5)
    return(round(longDecCel, 2))
    
print("80 fahrenheit = ", celsius(80), "celsius")

print("########################################################")









