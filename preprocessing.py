import json
import random
import nltk
import numpy as np
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression

nltk.download('punkt')
nltk.download('wordnet')

# Load dataset
with open("intents.json") as file:
    data = json.load(file)

lemmatizer = WordNetLemmatizer()

# Prepare training data
X_train = []
y_train = []
classes = []

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        tokens = nltk.word_tokenize(pattern.lower())  # Tokenization
        words = [lemmatizer.lemmatize(word) for word in tokens]  # Lemmatization
        X_train.append(" ".join(words))
        y_train.append(intent["tag"])

    if intent["tag"] not in classes:
        classes.append(intent["tag"])

# Convert text into numerical features
vectorizer = TfidfVectorizer()
X_train_tfidf = vectorizer.fit_transform(X_train)

# Train a Logistic Regression model
model = LogisticRegression()
model.fit(X_train_tfidf, y_train)
