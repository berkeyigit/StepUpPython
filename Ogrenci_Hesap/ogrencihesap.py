import matplotlib.pyplot as plt

class Student():
    def __init__(self,isim,soyisim,not1,not2,not3):
        self.isim = isim
        self.soyisim = soyisim
        self.not1 = not1
        self.not2 = not2
        self.not3 = not3
        self.ortalama = ((not1*0.3)+(not2*0.3)+(not3*0.4))
        self.durum = self.durum_hesapla()
        self.harf_notu = self.harf_notu_hesapla()
        

    def durum_hesapla(self):
        if self.ortalama >= 50:
            return "Gecti"
        else:
            return "Kaldi"
        
    def harf_notu_hesapla(self):
        if self.ortalama >= 85:
            return "AA"
        elif self.ortalama >= 70:
            return "BA"
        elif self.ortalama >= 60:
            return "BB"
        elif self.ortalama >= 50:
            return "CB"
        else:
            return "FF"
        
    def __str__(self):
        return f"{self.isim} {self.soyisim} - Not1: {self.not1}, Not2: {self.not2}, Not3: {self.not3}, Ortalama: {self.ortalama}, Durum: {self.durum}, Harf Notu: {self.harf_notu}"

def sirala(ogrenciler):
    return sorted(ogrenciler, key=lambda x: x.ortalama, reverse=True)

def ogrenci_ekle():
    isim = input("İsim: ")
    soyisim = input("Soyisim: ")
    not1 = float(input("Not 1: "))
    not2 = float(input("Not 2: "))
    not3 = float(input("Not 3: "))
    return Student(isim, soyisim, not1, not2, not3)
    

ogrenciler = []

while True:
    print("\n1 - Öğrenci Ekle")
    print("2 - Öğrencileri Listele")
    print("3 - Sınıf Ortalamasını Hesapla")
    print("4 - Geçenleri Listele")
    print("5 - Kalanları Listele")
    print("6 - Grafik Göster")
    print("7 - Çıkış")

    secim = input("Seçiminiz: ")

    if secim == "1":
        ogrenci = ogrenci_ekle()
        ogrenciler.append(ogrenci)
    elif secim == "2":
        print("Sirali Liste:")
        for ogrenci in ogrenciler:
            print(ogrenci)
    elif secim == "3":
        print("Sinif ortalamasi : ", sum(ogrenci.ortalama for ogrenci in ogrenciler) / len(ogrenciler))
    elif secim == "4":
        for ogrenci in ogrenciler:
            if ogrenci.durum == "Gecti":
                print(ogrenci)
    elif secim == "5":
        for ogrenci in ogrenciler:
            if ogrenci.durum == "Kaldi":
                print(ogrenci)
    elif secim == "6":
        for ogrenci in ogrenciler:
            if ogrenci.durum == "Gecti":
                plt.bar(ogrenci.isim, ogrenci.ortalama, color='green')
            else:
                plt.bar(ogrenci.isim, ogrenci.ortalama, color='red')
        ortalama = sum(ogrenci.ortalama for ogrenci in ogrenciler) / len(ogrenciler)
        plt.axhline(y=ortalama, color='yellow', linestyle='--')
        plt.xlabel('Öğrenciler')
        plt.ylabel('Not Ortalaması')
        plt.title('Öğrenci Not Ortalamaları')
        plt.show()
    
    elif secim == "7":
        break

        
# Daha ilerisi için DB ile birleştir Arayüz ekle. 