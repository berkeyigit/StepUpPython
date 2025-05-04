import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("spam_and_ham_sentences_1000.csv")

df["etiket"] = df["Label"].map({"spam": 1, "ham": 0})

df.rename(columns={"Sentence": "mail"}, inplace=True)

print(df.head())

x = df["mail"]
y = df["etiket"]

vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(x)

x_train, x_test, y_train, y_test = train_test_split(X_vectorized, y, test_size=0.2, random_state=42)

model = MultinomialNB()
model.fit(x_train, y_train)
y_pred = model.predict(x_test)
print("Doğruluk Skoru:", accuracy_score(y_test, y_pred))

yeni_mail = input("\nBir mail giriniz : ")
yeni_mail_vectorized = vectorizer.transform([yeni_mail])
tahmin = model.predict(yeni_mail_vectorized)
if tahmin[0] == 1:
    print("Spam maildir")
else:
    print("Spam değildir")
