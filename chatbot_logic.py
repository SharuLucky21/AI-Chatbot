import json
import random
import nltk
import numpy as np
from preprocessing import vectorizer, model, data  # Import trained model and data

nltk.download('punkt')

def chatbot_response(user_input):
    input_tfidf = vectorizer.transform([user_input])  # Convert input to TF-IDF
    predicted_tag = model.predict(input_tfidf)[0]  # Predict the intent

    # Get response based on predicted intent
    for intent in data["intents"]:
        if intent["tag"] == predicted_tag:
            return random.choice(intent["responses"])

    return "I'm not sure how to respond. Can you rephrase?"
