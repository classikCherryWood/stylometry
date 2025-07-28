from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

LINES = ['-', ':', '--']

def textToString(filename):
    """read a text file and return a string"""
    with open(filename) as f: 
        return f.read()

def makeWordDict(stringsByAuthor):
    """return dictionary of tokenised workds by corpus by author"""
    wordsByAuthor = dict()
    for author in stringsByAuthor:
        tokens = nltk.word_tokenize(stringsByAuthor[author])
        wordsByAuthor[author] = ([token.lower() for token in tokens
                                  if token.isalpha()])
    
if __name__ == "__main__":
    pass