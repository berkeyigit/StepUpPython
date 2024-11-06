#Veri setini pandas ile çek
#Kullanicinin listelemek istediği categoryi sor
#Bu kategoride alt kategorilere göre filmleri listele

import random
import pandas as pd

print("\n"+"*"*80+"\n")
print("\t\t~~~~~~   Movie_Smilator'a   ~~~~~~\n\t\t  ~~~~~~   Hos Geldiniz   ~~~~~~")
print("\n"+"*"*80+"\n")

df = pd.read_csv("movie_dataset.csv")
film_adi = df["Film Adı"]
Genre = df["Türü"]
Year = df["Yıl"]
imdb = df["Puan"]

print("Kategoriler : \n")
user_input = input("\tA) Türü\n\tB) Yıl\n\tC) Puan\n\nLütfen filmleri sıralamak istediğiniz kriteri yaziniz  : ").upper()
if user_input == 'A':
    categories = df["Türü"].unique()
    print("\nMevcut Kategoriler : ")
    
    for i,category in enumerate(categories,1):
        print(f"{i} - {category}")
    
    user_genre = int(input("Hangi kategoride filmleri görmek istersiniz : "))

    selected_category = categories[user_genre - 1]
    filtered_movies = df[df["Türü"] == selected_category]

    print("\n"+"*"*80)

    print(f"\n{selected_category} kategorisindeki filmler : \n")
    print(filtered_movies[["Film Adı","Yıl","Puan"]] , "\n")

elif user_input == "B":

    araliklar = [1970,1980,1990,2000,2010,2020]
    tags = ["1970-1980","1980-1990","1990-2000","2000-2010","2010-2020"]    
    df["Yıl Araligi"] = pd.cut(df["Yıl"],bins=araliklar, labels=tags,right=False)
    
    print("\nMevcut Yıl Araliklari : \n")
    for i,tag in enumerate(tags,1):
        print(f"{i} - {tag}")

    user_year = int(input("\nLütfen filmi aradiginiz yil araliginizi giriniz : "))

    selected_year = tags[user_year-1]
    filtered_movies = df[df["Yıl Araligi"] == selected_year] 

    print("\n"+"*"*80)

    print(f"\n{selected_year} araligindaki filmler : \n")
    print(filtered_movies[["Film Adı","Yıl","Puan"]],"\n")
    
elif user_input == "C":
    
    araliklar = [5,6,7,8,9,10]
    tags = ["5-6","6-7","7-8","8-9","9-10"]
    df["Puan Araligi"] = pd.cut(df["Puan"],bins=araliklar,labels=tags,right=False)

    print("\nMevcut Puan Araliklari : \n")
    for i,tag in enumerate(tags,1):
        print(f"{i} - {tag}")

    user_puan = int(input("\nLütfen aradiginiz filmin imdb araligini giriniz : "))

    selected_puan = tags[user_puan-1]
    filtered_points = df[df["Puan Araligi"] == selected_puan]

    print("\n"+"*"*80)

    print(f"\n{selected_puan} araligindaki fimler : \n")
    print(filtered_points[["Film Adı","Yıl","Puan"]],"\n")

else:
    print("Geçersiz bir seçim yaptınız. Lütfen tekrar deneyiniz.")

    
