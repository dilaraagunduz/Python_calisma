#--------------------------------------------
#OGRENCI KAYIT ve NOT YONETIM SISTEMI
#(Sadece Temel Pyhthon Komutları)
#--------------------------------------------

# 1 String İslemleri

ogrenci_adi= " dilara gunduz "
ogrenci_adi=ogrenci_adi.strip() #Baştaki ve sondaki boslukları kaldır.
ogrenci_adi=ogrenci_adi.upper() #Tüm değişkeni büyük harfe çevirir.

print(ogrenci_adi)

#---------------------------------------------
# 2 OGRENCI NUMARASI ve NOTLAR (TIP DONUSUMU)

ogrenci_no = "167"
ogrenci_no = int(ogrenci_no)

print(ogrenci_no)

notlar = [70,80,90]

#------------------------------------------------
# 3 OGRENCI BILGILERINI DICTIONARY'DE TUTMA

ogrenci ={
    "ad":ogrenci_adi,
    "no":ogrenci_no,
    "notlar":notlar
    }

#------------------------------------------------
# 4 LISTEDE BIRDEN FAZLA OGRENCI TUTMA

ogrenciler = []
ogrenciler.append("ogrenci") #string ifade olarak istediğin isimleri append ile istediğin isimleri ekle. 

#--------------------------------------------------
# 5 lISTE UZERINDE ELEMAN ISLEMLERI

notlar.append(89)
notlar.remove(80)
notlar.pop()
x=notlar.pop(1)  #x değişkenine sildiğin değeri atadığında daha sonra tekrar append komutu ile ekleyebilirsin.
notlar.append(x)

print(notlar)

#---------------------------------------------------
# 6 TUPLE ILE DERS BILGISI TUTMA

dersler = ("python","istatistik","veri_gorsel")
print(dersler)

#--------------------------------------------------
# 7 SET ile DERSE KAYITLI OGRENCI ANALIZI

python_dersi = {"Dilara","Elif","Şule"}
istatistik_dersi = {"Zeynep","Halime","Ali","Dilara"}

#Kesisim
ortak_ogrenciler = python_dersi.intersection(istatistik_dersi)
print(ortak_ogrenciler)

#Fark
fark_ogrenciler=python_dersi.difference(istatistik_dersi)
print(fark_ogrenciler)

#Birlesim
ortak_ogrenci = python_dersi.union(istatistik_dersi)
print(ortak_ogrenci)

#---------------------------------------------------
# 8 STRING SUBSTRING & REPLACE
isim = "Dilara,Zeynep"
isim[0:3]
print("İsmin ilk 3 harfi:",isim[0:3])

isim.replace("Dilara", "Duru")
#Komut yazma yerine burada degisken tanımlayarak ta yapabilirsin.
print("Güncel İsim:",isim.replace("Dilara", "Duru"))

#Program Çıktısı

print("Program başarıyla tanımlandı")

