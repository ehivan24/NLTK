'''
Created on May 25, 2015

@author: edwingsantos
'''

import nltk
import random
from nltk.corpus import movie_reviews

documents = [(list(movie_reviews.words(fileid)), catergory)
             for catergory in movie_reviews.categories()
             for fileid in movie_reviews.fileids(catergory)]

random.shuffle(documents)

#print(documents[1]) 
             
allwords = []

for w in movie_reviews.words():
    allwords.append(w.lower())
    
allwords = nltk.FreqDist(allwords)
#print allwords.most_common(15)


print allwords['good'] #how many times the word appers

word_features = list(allwords.keys()[:3000])

def findFeatures(document):
    words = set(document)
    features = {}
    for w in word_features:
        features[w] = (w in words)
        
    return features


print (findFeatures(movie_reviews.words('neg/cv027_26270.txt')))
featuresets = [(findFeatures(rev), category) for (rev, category) in documents]






