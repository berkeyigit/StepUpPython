import pandas as pd
import random

#Girizgah
print("*"*80+"\n")
print("\t\t\t\tİSİM - ŞEHİR - HAYVAN \n\t\t\t\tOYUNUNA HOŞ GELDİNİZ\n")
print("*"*80+"\n")
print("Oyundan Çıkmak İsterseniz 'Q' yazmaniz yeterli olacaktir.\n")

#Dataları ekliyoruz
data_files = {
    "isim": pd.read_csv("isimler.csv")["isim"].str.upper(),
    "sehir": pd.read_csv("turkiye_sehirleri.csv")["sehir"].str.upper(),
    "hayvan": pd.read_csv("hayvanlar.csv")["hayvan"].str.upper(),
    "bitki": pd.read_csv("bitki.csv")["bitki"].str.upper(),
    "ulke": pd.read_csv("ulkeler.csv")["ulke"].str.upper()
}


alfab = "ABCÇDEFGHIİJKLMNOÖPRŞSTUÜVYZ"
alfabe = [harf for harf in alfab]

puan = 0
round = 0
oyundan_cik = False

#Oyun Dongusu
while round < 10 and not oyundan_cik:

    #Program random olarak harfimizi seciyor
    chose_letter = random.choice(alfabe)
    print(f"\tHarfiniz : {chose_letter}\n")

    inputs = {}


    for category in data_files.keys():
        user_input = input(f"\n{chose_letter} ile başlayan bir {category} giriniz lütfen: ").upper()

        filtered_values = data_files[category][data_files[category].str.startswith(chose_letter)]
        if not filtered_values.empty:
            computer_choise = random.choice(filtered_values.values)
            print(f"\nBilgisayarin Cevabi : {computer_choise}")
        else:
            print(f"{chose_letter} ile başlayan bir {category} bulunmuyor")

        #Oyundan cikmak icin
        if user_input.upper() == "Q":
            oyundan_cik = True
            break

        elif user_input[0].upper() == chose_letter:

            if user_input in data_files[category].values:
                inputs[category] = user_input
                if computer_choise == user_input:
                    print(f"{category} doğru!")
                    print(f"Diger oyuncu(Computer) ile ayni {category} kullandiniz. Bu yüzden sadece 5 puan kazandiniz.\n")
                    puan += 5
                else:
                    print(f"{category} doğru!")
                    print("10 puan kazandiniz\n")
                    puan += 10
            else: 
                print(f"{user_input}, {category} listesinde bulunmuyor.")
        else:
            print(f"{user_input},{chose_letter} ile başlamıyor. ")
            
    print(f"Puaniniz : {puan}")
    round +=1
