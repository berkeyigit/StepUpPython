import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt

def döviz_ekle():

    döviz_kisaltma = " "
    dövizler = []

    while döviz_kisaltma != "Q".upper():
    
        print("Kaydetme ekranindan çikmak için 'Q' girmeniz yeterli.")
        döviz_kisaltma = input("Lütfen Eklemek istediginiz dövizin kisaltmasini giriniz : ").upper()

        if döviz_kisaltma != "Q":
            dövizler.append(döviz_kisaltma)

    df = pd.DataFrame(columns=["Döviz","Deger","Tarih"])
    df.to_csv("doviz.csv",index=False)

   

def döviz_güncelle():

    df = pd.read_csv("doviz.csv")
    dövizler = df["Döviz"].unique().tolist()
    döviz_kisaltma = input("Güncellemek istediginiz dövizin kisaltmasini giriniz : ").upper()

    if döviz_kisaltma in dövizler:
        deger = float(input(f"{döviz_kisaltma} için yeni degeri giriniz : "))
        tarih = datetime.now().strftime("%Y-%m-%d %H-%M-%S")

        yeni_veri = pd.DataFrame([[döviz_kisaltma,deger,tarih]],columns=["Döviz","Deger","Tarih"])
        yeni_veri.to_csv("doviz.csv",mode="a",header=False,index=False)
        print(f"{döviz_kisaltma} güncellendi : {deger} - {tarih}")
    else:
        print(f"{döviz_kisaltma} bulunamadi.")

def grafik():
    
    istek = input("Grafiğini istediğinizi dövizi seçiniz : ").upper()
    df = pd.read_csv("doviz.csv")
    df_selected = df[df["Döviz"] == istek]

    plt.plot(df_selected["Deger"], label="Döviz Degeri")
    plt.plot(df_selected["Tarih"], label ='Tarihleri')
    plt.xlabel("Deger")
    plt.ylabel("Tarih")
    plt.legend()
    plt.title(f"Döviz csv dosyasindan {istek} dövizinin tarihe göre degerleri")
    plt.show()

print("1 - Döviz Ekle\n2 - Döviz Güncelle\n3 - Secilen Dövizin Grafigini gör")

secim = input("Nasil bir islemde bulunmak istiyorsunuz ?")

if secim == "1":
    döviz_ekle()
elif secim == "2":
    döviz_güncelle()
elif secim == "3":
    grafik()
else:
    print("Geçersiz secim")


