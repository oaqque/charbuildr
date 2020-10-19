"""
Author: William Zhiwei Ye

Chatbot based on 
https://github.com/parulnith/Building-a-Simple-Chatbot-in-Python-using-NLTK/blob/master/chatbot.py

Harry Potter script from
https://www.kaggle.com/eward96/harry-potter-and-the-philosophers-stone-script
"""
import nltk
import numpy as np 
import pandas as pd
import random
import string # to process standard python strings
import os

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from sentiment import *
from chatbot import *

# Load Harry Potter corpus
os.chdir('../data')
data_dir = os.getcwd() + "/hp_script.csv"
corpus_df = pd.read_csv(data_dir, encoding = 'ISO-8859-1')
corpus = []
corpus_text = ''
sent_tokens = nltk.sent_tokenize('')

for line in corpus_df['dialogue']:
    corpus_text += line
corpus = nltk.sent_tokenize(corpus_text)

# Initialise sentiment analyzer
client = authenticate_client()

# --- Preprocessing --- #
# Required for the first time
# nltk.download('punkt') 
# nltk.download('wordnet')
# Wordnet is a semantically-oriented dictionary of English included in NLTK
lemmer = nltk.stem.WordNetLemmatizer()
# Takes tokens as input and returns normalized tokens
def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]
# Creates a mapping between punctuation and None 
# Ord creates an integer representing the unicode character
remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))

# Define a tfidf Vectorizer
TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words = 'english')
TfidfVec.fit(corpus)
corpus_tfidf = TfidfVec.transform(corpus)

# Determine the similarity of the user_response with the corpus
def determine_response(user_response):
    sent_tokens.append(user_response)
    user_response = [user_response]
    
    response_tfidf = TfidfVec.transform(user_response)
    # Determine cosine similarity between user_response and corpus
    cos = cosine_similarity(response_tfidf, corpus_tfidf).flatten()
    cos.sort()
    similarity = cos[-2]
    return similarity

def farewell():
    print("See ya! \n")

# Response generation for information retrieval
def response_inforet(user_response):
    robo_response = ''
    user_response = [user_response]

    tfidf = TfidfVec.transform(user_response)
    # Determine cosine similarity between user_response and corpus
    cos = cosine_similarity(tfidf, corpus_tfidf).flatten()
    idx = cos.argmax()

    robo_response = robo_response + corpus[idx] + "\n"
    print(robo_response)

def response_generative(user_response):
    print("This is a generative response \n")
    
# Main Function for Chatbot
flag = True
bot = ChatBot(corpus)
print("Bot: Hi, I'm the Harry Potter Bot \n")

while (flag == True):
    user_response = input("User Input: ")
    print("\n")
    user_response = user_response.lower()

    sim_calc = determine_response(user_response)
    # Pass the response from the user to the sentiment analysis endpoint
    sentiment = sentiment_analysis(client, [user_response])
    print("User Relationship: " + str(bot.update_user_relationship(sentiment)))

    if (sim_calc >= 0.2):
        response_inforet(user_response)
    else:
        response_generative(user_response)

    if (user_response == 'bye'):
        flag = False 
        farewell()

