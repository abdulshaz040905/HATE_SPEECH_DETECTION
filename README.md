# Hate Speech Detection System

An AI-powered web application that detects **Hate Speech, Offensive Language, or Normal text** from user input using Natural Language Processing (NLP) and Machine Learning.

This project trains a machine learning model on a labeled dataset of tweets and provides **real-time predictions through a web interface**.

---

## Project Overview

Online platforms receive millions of comments daily, and detecting harmful language manually is difficult.
This project automatically classifies text into three categories:

* **Hate Speech**
* **Offensive Language**
* **Normal / Neither**

The system uses **TF-IDF vectorization with Logistic Regression** to analyze text and classify it.

---

## Features

* Machine Learning based hate speech detection
* Real-time prediction through a web interface
* REST API built using Flask
* Clean and modular project structure
* Text preprocessing for better accuracy
* Handles user input dynamically
* Easy to extend to social media platforms

---

## Technologies Used

### Programming

* Python
* JavaScript

### Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Logistic Regression

### Backend

* Flask
* Flask-CORS

### Frontend

* HTML
* CSS
* JavaScript

### Libraries

* pandas
* numpy
* scikit-learn
* pickle
* regex

---

## Project Structure

```
hate-speech-detection/
│
├── dataset.csv
├── train_model.py
├── model.pkl
├── vectorizer.pkl
├── app.py
│
└── frontend/
      ├── index.html
      ├── script.js
      └── style.css
```

---

## How It Works

1. Dataset containing tweets and labels is loaded.
2. Text is cleaned using preprocessing techniques.
3. TF-IDF converts text into numerical features.
4. Logistic Regression model is trained.
5. Model and vectorizer are saved.
6. Flask API loads the model and exposes a prediction endpoint.
7. Frontend sends user input to the API.
8. API returns the predicted class.

---

## Machine Learning Pipeline

```
Dataset
   ↓
Text Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Train-Test Split
   ↓
Logistic Regression Model
   ↓
Model Evaluation
   ↓
Save Model
```

---

## Installation

### 1. Clone the Repository

```
git clone https://github.com/yourusername/hate-speech-detection.git
```

```
cd hate-speech-detection
```

---

### 2. Install Dependencies

```
pip install pandas scikit-learn flask flask-cors
```

---

### 3. Train the Model

```
python train_model.py
```

This generates:

```
model.pkl
vectorizer.pkl
```

---

### 4. Run the Backend Server

```
python app.py
```

Server runs at:

```
http://127.0.0.1:5000
```

---

### 5. Run the Frontend

Open:

```
frontend/index.html
```

or run a local server:

```
python -m http.server
```

---

## API Endpoint

### Predict Hate Speech

**POST**

```
/predict
```

Request Body:

```
{
"text": "I hate you"
}
```

Response:

```
{
"prediction": "Hate Speech"
}
```

---

## Example Predictions

Input:

```
I hate you
```

Output:

```
Hate Speech
```

Input:

```
You idiot
```

Output:

```
Offensive Language
```

Input:

```
Have a nice day
```

Output:

```
Normal
```

---

## Model Evaluation Metrics

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

These metrics help evaluate the performance of the classification model.

---

## Future Improvements

* Use **BERT or Transformers for better accuracy**
* Real-time Twitter hate speech detection
* Chrome extension to detect harmful comments
* Multilingual hate speech detection
* Admin dashboard for monitoring flagged comments
* Deploy using Docker and cloud platforms

---

## Applications

* Social media moderation
* Online community management
* Comment filtering systems
* Cyberbullying detection
* Content moderation tools

---

## Author

Abdul Shaz

Information Science Student
Interested in AI, Machine Learning, and Full Stack Development

---

## License

This project is for educational and research purposes.
