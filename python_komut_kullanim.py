#-------------------------------
#METIN VERİ&DUZENLEYICI
#-------------------------------

#1 Metin islemleri bölümü
  #a)Bosluksuz inputa ifade yazdırma komutu
  
text = input("Bir metin giriniz:" ) 
text = input("Bir metin giriniz: ").strip()
print(text)

#Burada bir metin giriniz ifadesi tırnak içinde 
#sen eğer bu inputa değer atadığında tırnak içinde yazarsan tırnağı da karakter algılar.

    #b)Girilen inputu büyük harfe çevirerek  yazdırma komutu

text = input("Bir metin giriniz:" ) 
text = input("Bir metin giriniz: ").upper()
print(text)

    #b)Girilen inputu küçük harfe çevirerek  yazdırma komutu
    
text = input("Bir metin giriniz:" ) 
text = input("Bir metin giriniz: ").lower()
print(text)

    #c)Girilen inputun uzunlugunu yazdırma komutu

text = input("Bir metin giriniz:" ) 
text =len(input("Bir metin giriniz: "))
print(text)

    #c)Girilen inputta harf/kelime değiştirme komutu

text = input("Bir metin giriniz:" ) 
yeni_text = text.replace("dilara", "duru")
print("Eski Hali : ",text)
print("Yeni Hali : ",yeni_text)

    #d)Girilen inputun ilk 10 karekterini bulma komutu

text = input("Bir metin giriniz:" ) 
text=text[:10]
print(text)

text = input("Bir metin giriniz:" )
text=print(text[:10]) 
#Bu şekilde kullanırsan console da sana çıktı verir ama variable type olarak yukarıya değer atamaz.
#Cunku python önce text[:10] kısmını hesaplar.Bunu ekrana yazdırır.
#Ancak print() fonksiyonu işini bitirince geriye None (boş/hiçlik) değerini döndürür.
#Bu kod değerini alıp tekrar text değişkeninin içine koyar.

#-----------------------------------------------------------------
#2 Sayı Tip Degiştirme

age =input("Yaşınızı giriniz: ")
age =int(age) + 5 

#Burada string değeri integer değere çevirerek kişinin 5 yıl sonraki yaşını hesaplayan komut yazdık. 

#-----------------------------------------------------------------
#3 Liste İslemleri (Alısveris Listesi Olusturma)

shopping_list = ["elma","armut","muz","ananas"]
shopping_list.append("mango")
shopping_list.remove("muz")
shopping_list.insert(2, "çilek")
shopping_list.pop(0)
shopping_list[0:3]

#-----------------------------------------------------------------
#4 TUPLE OLUSTURMA

t=("dilara","gunduz",31)
t[0]

#Burada tuple ları komutlarla değiştiremeyeceğimizi gördük.

#-----------------------------------------------------------------
#5 SÖZLÜK (DICTIONARY) OLUSTURMA

Sozluk = {"name": "dilara",
          "surname": "gunduz",
          "age": 21,
          "city" :"Istanbul"
          }

Sozluk["school"] = "Istanbul Univercity"
Sozluk

Sozluk["name"] = "Duru"
Sozluk

Sozluk["name"]

#-----------------------------------------------------------------
#5 SET (KÜME)

languages = {"Python","Java","C"}
required = {"Python","SQL"}

languages.add("SQL")
languages.remove("Java")

languages.difference(required)
required.difference(languages)

languages.intersection(required)
languages.union(required)
