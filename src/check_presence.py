# Author: William Ye
# Check for the presence of generated conversations in the original training data

# Import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
import os
import pandas as pd

# Initialised TFIDF Vectorizer
vectorizer = TfidfVectorizer()

# Prepare training corpus tfidf vectors
corpus_raw = pd.read_csv()
tfidf_corpus = []
for row in corpus_raw: 
    utterance = row['line']
    tfidf = vectorizer.fit_transform([utterance])
    tfidf_corpus.append(tfidf)

corpus_raw['tfidf'] = tfidf_corpus

directory_path = './output/agent-conversations/'
for file in os.scandir(directory_path):
    print(file.path)
    with open(file.path, 'r') as f: 
        for line in f: 
            tfidf = vectorizer.fit_transform([line])
            print(tfidf)
