import random
import pandas as pd
from colorama import Fore,Style,init  

init(autoreset=True)

#Girizgah
print("\n"+"*"*83+"\n")
print("KELİME OYUNUNA HOS GELDİNİZ\n")
print("*"*83+"\n")
print("Bu oyunda rastgele bir kelimeniz olacak.Deneme hakkiniz da harf sayiniz kadar olacak.")
print("Eğer geçmiş denediğiniz harflerin listesini görmek isterseniz 'memory' yazmaniz yeterli.\n")
print("Hazirsaniz başlayalim: \n")

#Pandas ile kelime yükleme ve seçme
wordlist = pd.read_csv("turkish_wordlist.csv")
words = wordlist.iloc[:,0].tolist()
word = random.choice(words).upper()

#Hak ve oyun tahtasi olusumu
life = len(word) 
memory = []
board = ""
for letter in word:
        board += "_"
print("*"*83+"\n")
print("KELİMENİZ {} harfli.\n".format(len(word)))
print("*"*83+"\n")

#Oyun döngüsü
while life > 0 and "_" in board:
        
    usertry = input("Lütfen {} harfli bir kelime tahmin ediniz: ".format(len(word))).upper()

    if usertry == "memory".upper():
            print("Daha önce ki denediginiz ve olmayan harfler: \n")     
            print(memory)

        
    if len(usertry) != len(word):
            print("\nLütfen harf sayisini dogru giriniz. Olmasi gereken harf sayisi = {}\n".format(len(word)))
            continue
        
    #Renkler ile oyuncuya bilgi verme
    display_board = ""
    for i in range(len(word)):
        if usertry[i] == word[i]:
                display_board += Fore.GREEN + usertry[i] + Style.RESET_ALL
        elif usertry[i] in word:
                display_board += Fore.YELLOW + usertry[i] + Style.RESET_ALL
        else:
                display_board += Fore.WHITE + usertry[i] + Style.RESET_ALL
                memory.append(usertry[i])
    
    print("\n"+ display_board + "\n")

    if life == 2:
        print("*** Son bir hakkiniz Kaldi ***\n")

    if usertry == word:
        print("*"*83+"\n")
        print("Tebrikler. Kazandiniz !!\n")
        print("*"*83+"\n")
        break
    else:
        life -=1

    if life == 0:
        print("*"*83+"\n")
        print("Üzgünüm. Kaybettiniz.\n")
        print(f"Doğru kelime {word} idi")
        print("*"*83+"\n")

                
                

    