import random
import pandas as pd

print("*"*80+"\n")
print("\t\t\t ~~~ ANAGRAM OYUNUNA ~~~ \n\t\t\t  ~~~ HOŞ GELDİNİZZ ~~~\n")
print("*"*80+"\n")

print("Size Karistirilmis olarak verilen harflerden dogru kelimeyi tahmin etmeniz gerekiyor.")
print("Oyundan Cikmak icin ya da bir üst menüye dönmek için 'Q' tusuna basiniz...")

df = pd.read_csv("turkish_wordlist.csv")
easy_anagram = []
normal_anagram = []
hard_anagram = []

for word in df['kelime']:
    if len(word) < 5:
        easy_anagram.append(word)
    elif len(word) <8:
        normal_anagram.append(word)
    else:
        hard_anagram.append(word)

def anagram_game(word_list,difficulty_name):
    hp = 3
    select_word = random.choice(word_list).upper()
    joker = list(select_word)
    random.shuffle(joker)
    joker = ''.join(joker)

    while hp>0:

        print(f"\nVerilen Harfleriniz ({difficulty_name}) : {joker}\nDoğru siraya koymakta iyi şanslar!\n")
        print("*"*80+"\n")
        user_forecast = input("Tahminizi alalim : ").upper()

        if user_forecast == 'Q':
            print("Oyun Sonlandiriliyor...")
            break
        
        if user_forecast == select_word:
            print("\n"+"*"*30+"\n")
            print("Tebrikler ! Doğru bildiniz.\n")
            print("*"*30+"\n")
            break

        else:
            print(f"Bu turu kaybettiniz. Ama üzülmeyin {hp-1} hakkiniz daha var.")
            hp -=1

        if hp == 0:
                print(f"Başaramadiniz. Doğru anagram {select_word} idi")
                break
        



while True:
    mode_selection = input("\n\t1 - Easy Anagram\n\t2 - Normal Anagram\n\t3 - Hard Anagram\n\n\tLütfen zorluk seviyenizi seçiniz: \n\t")

    
    if mode_selection == "Q":
        print("Oyun Sonlandiriliyor...")
        break
    if mode_selection == "1":
        anagram_game(easy_anagram,"EASY")
    elif mode_selection == '2':
        anagram_game(normal_anagram,"NORMAL")
    elif mode_selection == "3":
        anagram_game(hard_anagram,"HARD")
    else:
        print("Geçersiz bir harf girdiniz.Lütfen tekrar deneyiniz : ")
        continue