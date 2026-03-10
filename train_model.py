import pandas as pd
import re
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

data = pd.read_csv("dataset.csv")

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+", "", text)
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^a-z\s]", "", text)
    return text

data["tweet"] = data["tweet"].apply(clean_text)

X = data["tweet"]
y = data["class"]

vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = LogisticRegression(max_iter=2000,class_weight="balanced")

model.fit(X_train,y_train)

print("Model trained")

pickle.dump(model,open("model.pkl","wb"))
pickle.dump(vectorizer,open("vectorizer.pkl","wb"))