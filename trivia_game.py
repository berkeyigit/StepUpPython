#sorular ve cevaplarını içeren bir sözlük oluşturulacak ve şıklar eklenecek
#Random olarak belli bir sayida soru seçilecek
#Joker hakları eklenecek
#Bilinen soru sayısına göre score yazılacak
#SQL öğrenince scoreboard ekle!!

import random
import pandas as pd

print("*"*80+"\n")
print("\t\t| ~~~ TRİVİA OYUNUNA HOS GELDİNİZ ~~~ |\n")
print("*"*80+"\n")

df = pd.read_csv("sorular.csv")
questions = dict(zip(df["soru"],zip(df["secenek_a"],df["secenek_b"],df["secenek_c"],df["secenek_d"],df["dogru_cevap"])))

print("Lütfen gelen sorulara dogru cevap vermeye calisiniz... ")
print("3 adet jokeriniz olacak. Bunlar, 'PAS','CHANGE','HALF' yazarak kullanabilirsiniz.\n")
print("\t'PAS' jokeri soruyu geçmenizi sağlar.\n\t'CHANGE' jokeri soruyu değiştirmenizi sağlar.\n\t'HALF' jokeri ise şiklari yariya indirmenizi saglar.\n")
print("Eger hazirsaniz sorularimiza gecelim : ")
soru = 0
half_joker = 1
pas_joker = 1
change_question = 1
puan = 0
while soru < 10:

    print(f"\n{soru+1}. Soru: \n")

    question,options = random.choice(list(questions.items()))
    print(f"Soru: {question}")
    print("A : ",options[0])
    print("B : ",options[1])
    print("C : ",options[2])
    print("D : ",options[3])
    
    correct_answer_value = options[4]
    answer = input("Lütfen Dogru Secenegi Yaziniz (A, B, C, D): \n").upper()

    if answer == "PAS" and pas_joker >0:
        print("\nBu soruyu geçtiniz. Yeni sorunuz geliyor...")
        soru +=1
        pas_joker -=1
        continue
    elif answer == "CHANGE" and change_question >0:
        print("\nBu soruyu Değiştirdiniz. Yeni sorunuz geliyor.")
        change_question -=1
        continue
    elif answer == "HALF":
        print("\nYanlis siklarin yarisi gidiyor.")
        half_joker -=1
        all_options = ["A","B","C","D"]
        correct_option_index = options.index(correct_answer_value)
        correct_option = all_options[correct_option_index]

        wrong_options = [opt for opt in all_options if opt != correct_option] 
        removed_options = random.sample(wrong_options,2)

        print(f"Soru: {question}")
        for opt in all_options:
            if opt not in removed_options:
                print(f"{opt} : {options[all_options.index(opt)]}")
        
        answer = input("Lütfen Dogru seceneği yaziniz (A, B, C, D)\n").upper()

    if (answer == "A" and options[0] == correct_answer_value) or \
        (answer == "B" and options[1] == correct_answer_value) or \
        (answer == "C" and options[2] == correct_answer_value) or \
        (answer == "D" and options[3] == correct_answer_value):
        print("\nTebrikler. Doğru cevap verdiniz. Sonraki soruya geçiliyor.")
        soru +=1
        if soru < 4:
            puan += 10
        elif soru < 8:
            puan += 25
        else:
            puan += 50
    else:
        print(f"\nYanildiniz. Dogru cevap : {correct_answer_value}\n")
        print(f"Şuana kadar kazandiginiz puan : {puan}")
        break

    if soru == 10:
        print("TEBRİKLER. OYUNU KAZANDİNİZ")
        if pas_joker == 1:
            puan += 25
        
        if change_question == 1:
            puan += 25

        if half_joker == 1:
            puan += 25
        
        print(f"Scorunuz : {puan}")