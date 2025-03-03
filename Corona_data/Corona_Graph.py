import pandas as pd
import tkinter as tk
from tkinter import ttk,messagebox
import time
import matplotlib.pyplot as plt 
import numpy as np
def manuel():

    gun_sayisi = int(input("Kaç günlük veri girmek istiyorsunuz? "))

    gunler = []
    vakalar = []
    olumler = []

    for i in range(gun_sayisi):
        gun = input(f"{i+1}. gün adı: ")
        vaka = int(input(f"{gun} günü vaka sayısı: "))
        olum = int(input(f"{gun} günü ölüm sayısı: "))

        gunler.append(gun)
        vakalar.append(vaka)
        olumler.append(olum)

    plt.figure(figsize=(10, 5))
    plt.plot(gunler, vakalar, marker="o", linestyle="-", color="blue", label="Vaka Sayısı")
    plt.plot(gunler, olumler, marker="o", linestyle="-", color="red", label="Ölüm Sayısı")

    plt.title("Günlük Korona Verileri", fontsize=14)
    plt.xlabel("Günler", fontsize=12)
    plt.ylabel("Sayı", fontsize=12)
    plt.xticks(rotation=45) 
    plt.legend() 
    plt.grid(True)

    plt.show()

def korona_veri_girisi():

    df = pd.read_csv("korona_verisi.csv")
    df = df.replace(np.nan, 0)

    df["Tarih"] = pd.to_datetime(df["Tarih"],dayfirst=True)
    df = df.sort_values("Tarih")

    root = tk.Tk()
    root.title("Korona Veri Girişi")
    root.geometry("400x200")

    date_list = df["Tarih"].astype(str).tolist()

    tk.Label(root, text="Başlangıç Tarihi Seç:").pack()
    combobox1 = ttk.Combobox(root,values=date_list,state="readonly")
    combobox1.pack()

    tk.Label(root, text="Bitiş Tarihi Seç:").pack()
    combobox2 = ttk.Combobox(root,values=date_list,state="readonly")
    combobox2.pack()

    def grafik_goster():
        secili_tarih1 = combobox1.get()
        secili_tarih2 = combobox2.get()

        if not secili_tarih1 or not secili_tarih2:
            messagebox.showerror("Hata", "Lütfen iki tarih seçin!")
            return

        tarih1 = pd.to_datetime(secili_tarih1)
        tarih2 = pd.to_datetime(secili_tarih2)

        df_filtered = df[(df["Tarih"] >= tarih1) & (df["Tarih"] <= tarih2)]

        fig,axs = plt.subplots(2,1, figsize=(10, 6))

        axs[0].plot(df_filtered["Tarih"], df_filtered["Toplam Vaka"], marker="o", linestyle="-", color="blue", label="Vaka Sayısı")
        axs[0].set_title("Vaka Sayıları")
        axs[0].set_xlabel("Tarih")
        axs[0].set_ylabel("Vaka Sayısı")
        axs[0].legend()
        axs[0].grid(True)

        axs[1].plot(df_filtered["Tarih"], df_filtered["Toplam_Vefat"], marker="o", linestyle="-", color="red", label="Ölüm Sayısı")
        axs[1].set_title("Ölüm Sayıları")
        axs[1].set_xlabel("Tarih")
        axs[1].set_ylabel("Ölüm Sayısı")
        axs[1].legend()
        axs[1].grid(True)

        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    
    btn = tk.Button(root, text="Karşılaştır", command=grafik_goster)
    btn.pack(pady=10)

    root.mainloop()

korona_veri_girisi()