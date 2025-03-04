import json
import pickle
import random

import numpy as np
import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model

model = load_model("Neural Network Chatbot\\chatbot.h5")
intents = json.load(open("Neural Network Chatbot\\intents.json"))
words = pickle.load(open("Neural Network Chatbot\\words.pkl", "rb"))
classes  = pickle.load(open("Neural Network Chatbot\\classes.pkl", "rb"))
lemmatizer = WordNetLemmatizer()

def preprocess(sentence):
    word_list = nltk.word_tokenize(sentence)
    word_list = [lemmatizer.lemmatize(word.lower()) for word in word_list]
    return word_list

def bag_to_word(sentence):
    word_list = preprocess(sentence)
    bag = [1 if word in word_list else 0 for word in words]
    return np.array(bag)

def get_predictions(sentence):
    bow = bag_to_word(sentence)
    predictions = model.predict(np.array([bow]))[0]
    index = np.argmax(predictions)
    return classes[index] if predictions[index] > 0.25 else "Sorry!. I cannot understand."

def get_answer(tag):
    for intent in intents["intents"]:
        if intent["tag"] == tag:
            return random.choice(intent["responses"])
        
def chatbot():
    while True:
        user_input = input("You : ")
        
        if user_input.lower() == "quit":
            print("Bot : Goodbye!")
            break
        
        tag = get_predictions(user_input)
        answer = get_answer(tag)
        print(f"Bot : {answer}")
        
if __name__ == "__main__":
    chatbot()