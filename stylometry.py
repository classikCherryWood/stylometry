from collections import Counter
import matplotlib.pyplot as plt
import nltk
from nltk.corpus import stopwords

LINES = ['-', ':', '--']


def textToString(filename):
    """read a text file and return a string"""
    with open(filename, encoding='utf-8', errors='ignore') as f: 
        return f.read()

def makeWordDict(stringsByAuthor):
    """return dictionary of tokenised workds by corpus by author"""
    wordsByAuthor = dict()
    for author in stringsByAuthor:
        tokens = nltk.word_tokenize(stringsByAuthor[author])
        wordsByAuthor[author] = ([token.lower() for token in tokens
                                  if token.isalpha()])
def main():
    stringsByAuthor = dict()
    stringsByAuthor['doyle'] = textToString('hound.txt')
    stringsByAuthor['wells'] = textToString('war.txt')
    stringsByAuthor['unknown'] = textToString('lost.txt')

    print(stringsByAuthor['doyle'][:300])

    wordsByAuthor = makeWordDict(stringsByAuthor)
    
    
if __name__ == "__main__":
    main()