import os
import nltk
import pandas as pd
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils import generate_rs_threshold

class RetrievalModel():
    def __init__(self):
        # --- Preprocessing --- #
        # Required for the first time
        # nltk.download('punkt') 
        # nltk.download('wordnet')
        # Wordnet is a semantically-oriented dictionary of English included in NLTK    
        self.corpus = self.load_corpus()
        self.relationship_score_threshold = generate_rs_threshold()
        self.TfidfVec = TfidfVectorizer(tokenizer = self.LemNormalize, stop_words = 'english')
        self.corpus_tfidf = self.calculate_corpus_tfidf(self.corpus)

    def LemTokens(self, tokens):
        """Takes tokens as input and returns normalized tokens"""
        lemmer = nltk.stem.WordNetLemmatizer()
        return [lemmer.lemmatize(token) for token in tokens]

    def LemNormalize(self, text):
        """Creates a mapping between punctuation and None""" 
        remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)
        return  (nltk.word_tokenize(text.lower().translate(remove_punct_dict)))
    
    def load_corpus(self):
        # Load Harry Potter corpus
        os.chdir('data/csv')
        data_dir = os.getcwd() + "/hp_script.csv"
        corpus_df = pd.read_csv(data_dir, encoding = 'ISO-8859-1')
        corpus = []
        corpus_text = ''

        for line in corpus_df['dialogue']:
            corpus_text += line
        corpus = nltk.sent_tokenize(corpus_text)
        return corpus
    
    def calculate_corpus_tfidf(self, corpus):
        tfidf = self.TfidfVec.fit_transform(corpus)
        return tfidf

    # Determine the similarity of the user_response with the corpus
    def calculate_similarity(self, user_response):
        user_response = [user_response]
        
        response_tfidf = self.TfidfVec.transform(user_response)
        # Determine cosine similarity between user_response and corpus
        cos = cosine_similarity(response_tfidf, self.corpus_tfidf).flatten()
        cos.sort()
        similarity = cos[-2]
        return similarity

    def farewell(self):
        print("See ya! \n")

    # Response generation for information retrieval
    def get_response(self, user_response):
        response = ''

        tfidf = self.TfidfVec.transform([user_response])
        # Determine cosine similarity between user_response and corpus
        cos = cosine_similarity(tfidf, self.corpus_tfidf).flatten()
        idx = cos.argmax()

        response = response + self.corpus[idx]
        return response
