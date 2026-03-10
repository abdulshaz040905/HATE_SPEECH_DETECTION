from flask import Flask, request, jsonify
from flask_cors import CORS
import pickle
import re

app = Flask(__name__)
CORS(app)   # enable CORS

model = pickle.load(open("model.pkl","rb"))
vectorizer = pickle.load(open("vectorizer.pkl","rb"))

def clean_text(text):
    text = text.lower()
    text = re.sub(r"http\S+","",text)
    text = re.sub(r"@\w+","",text)
    text = re.sub(r"[^a-z\s]","",text)
    return text

@app.route("/predict", methods=["POST"])
def predict():

    data = request.json
    text = data["text"]

    text = clean_text(text)

    text_vec = vectorizer.transform([text])

    prediction = model.predict(text_vec)[0]

    labels = {
        0: "Hate Speech",
        1: "Offensive Language",
        2: "Normal"
    }

    return jsonify({"prediction": labels[prediction]})

if __name__ == "__main__":
    app.run(debug=True)