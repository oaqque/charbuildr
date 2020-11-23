# Author: William Ye
# Check for the presence of generated conversations in the original training data

# Import libraries
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os
import pandas as pd
from tqdm import tqdm
import numpy as np

# Initialised TFIDF Vectorizer
vectorizer = TfidfVectorizer()

# Prepare training corpus tfidf vectors
corpus_raw = pd.read_csv('../trainer/corpus/rick_script_clean.csv')
tfidf_corpus = []
for row in tqdm(corpus_raw['line']): 
    tfidf = vectorizer.fit_transform([row])
    tfidf_corpus.append(tfidf)

corpus_raw['tfidf'] = tfidf_corpus

# Define functions used in this file
def get_most_similar(line):
    similarities = []
    try:
        for row in corpus_raw['line']:
            similarities.append(compute_similarity(line, row))
        index = getArgmax(similarities)
        return corpus_raw['line'][index]
    except:
        return "Could not compute similarity"

def getArgmax(list): 
    return np.asarray(list).argmax()

def compute_similarity(x, y):
    from nltk.corpus import stopwords 
    from nltk.tokenize import word_tokenize 
    
    # tokenization 
    X_list = word_tokenize(x.lower())  
    Y_list = word_tokenize(y.lower()) 
    
    # sw contains the list of stopwords 
    sw = stopwords.words('english')  
    l1 =[];l2 =[] 
    
    # remove stop words from the string 
    X_set = {w for w in X_list if not w in sw}  
    Y_set = {w for w in Y_list if not w in sw} 
    
    # form a set containing keywords of both strings  
    rvector = X_set.union(Y_set)  
    for w in rvector: 
        if w in X_set: l1.append(1) # create a vector 
        else: l1.append(0) 
        if w in Y_set: l2.append(1) 
        else: l2.append(0) 
    c = 0
    
    # cosine formula  
    for i in range(len(rvector)): 
            c+= l1[i]*l2[i] 
    cosine = c / float((sum(l1)*sum(l2))**0.5) 
    return cosine

# Get the most similar lines
output_line = []
output_similar_line = []
directory_path = './output/agent-conversations/'
for file in tqdm(os.scandir(directory_path)):
    with open(file.path, 'r') as f: 
        for line in f: 
            output_line.append(line)
            output_similar_line.append(get_most_similar(line))

d = {'line': output_line, 'similar_line': output_similar_line}
output_df = pd.DataFrame(d)
output_df.to_csv('./output/presence/test.csv')
print(output_df.head())